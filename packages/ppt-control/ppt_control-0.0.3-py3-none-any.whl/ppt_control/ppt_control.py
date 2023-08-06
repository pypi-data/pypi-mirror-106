import sys
sys.coinit_flags= 0
import win32com.client
import pywintypes
import os
import shutil
#import http.server as server
import socketserver
import threading
import asyncio
import websockets
import logging, logging.handlers
import json
import urllib
import posixpath
import time
import pythoncom
import pystray
import tkinter as tk
from tkinter import ttk
from PIL import Image
from copy import copy

import ppt_control.http_server_39 as server
import ppt_control.config as config

logging.basicConfig()

global http_daemon
global ws_daemon
global STATE
global STATE_DEFAULT
global current_slideshow
global interface_root
global interface_thread
global logger
global refresh_daemon
global status_label
global http_label
global ws_label
global reset_ppt_button
global http_server
global icon
scheduler = None
current_slideshow = None
interface_root = None
interface_thread = None
CONFIG_FILE = r'''..\ppt-control.ini'''
LOGFILE = r'''..\ppt-control.log'''
logger = None
refresh_daemon = None
status_label = None
http_label = None
ws_label = None
ws_daemon = None
http_server = None
reset_ppt_button = None
icon = None


class Handler(server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.realpath(__file__)) + r'''\static''')
        
    def log_request(self, code='-', size='-'):
        return

        
    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        # abandon query parameters
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]
        # Don't forget explicit trailing slash when normalizing. Issue17324
        trailing_slash = path.rstrip().endswith('/')
        try:
            path = urllib.parse.unquote(path, errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)
        words = path.split('/')
        words = list(filter(None, words))
        if len(words) > 0 and words[0] == "cache":
            black = 0
            if current_slideshow:
                try:
                    path = config.prefs["Main"]["cache"] + "\\" + current_slideshow.name()
                except Exception as e:
                    path = "black.jpg"
                    logger.warning("Failed to get current slideshow name: ", e)
            else:
                path = "black.jpg"
                return path
            words.pop(0)
        else:
            path = self.directory
        for word in words:
            if os.path.dirname(word) or word in (os.curdir, os.pardir):
                # Ignore components that are not a simple file/directory name
                continue
            path = os.path.join(path, word)
        if trailing_slash:
            path += '/'
        return path


def run_http():
    global http_server
    http_server = server.HTTPServer((config.prefs["HTTP"]["interface"], config.prefs.getint("HTTP", "port")), Handler)
    http_server.serve_forever()

STATE_DEFAULT = {"connected": 0, "current": 0, "total": 0, "visible": 0, "name": ""}
STATE = copy(STATE_DEFAULT)
USERS = set()


def state_event():
    return json.dumps({"type": "state", **STATE})


def notify_state():
    global STATE
    if current_slideshow and STATE["connected"] == 1:
        try:
            STATE["current"] = current_slideshow.current_slide()
            STATE["total"] = current_slideshow.total_slides()
            STATE["visible"] = current_slideshow.visible()
            STATE["name"] = current_slideshow.name()
        except Exception as e:
            logger.info("Failed to update state variables, presumably PPT instance doesn't exist anymore: {}".format(e))
            current_slideshow.unload()
    else:
        STATE = copy(STATE_DEFAULT)
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        loop.call_soon_threadsafe(ws_queue.put_nowait, state_event())



async def ws_handler(websocket, path):
    logger.debug("Handling WebSocket connection")
    recv_task = asyncio.ensure_future(ws_receive(websocket, path))
    send_task = asyncio.ensure_future(ws_send(websocket, path))
    done, pending = await asyncio.wait(
        [recv_task, send_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()

async def ws_receive(websocket, path):
    logger.debug("Received websocket request")
    USERS.add(websocket)
    try:
        # Send initial state to clients on load
        notify_state()
        async for message in websocket:
            logger.debug("Received websocket message: " + str(message))
            data = json.loads(message)
            if data["action"] == "prev":
                if current_slideshow:
                    current_slideshow.prev()
                notify_state()
            elif data["action"] == "next":
                if current_slideshow:
                    current_slideshow.next()
                notify_state()
            elif data["action"] == "first":
                if current_slideshow:
                    current_slideshow.first()
                notify_state()
            elif data["action"] == "last":
                if current_slideshow:
                    current_slideshow.last()
                notify_state()
            elif data["action"] == "black":
                if current_slideshow:
                    if current_slideshow.visible() == 3:
                        current_slideshow.normal()
                    else:
                        current_slideshow.black()
                notify_state()
            elif data["action"] == "white":
                if current_slideshow:
                    if current_slideshow.visible() == 4:
                        current_slideshow.normal()
                    else:
                        current_slideshow.white()
                notify_state()
            elif data["action"] == "goto":
                if current_slideshow:
                    current_slideshow.goto(int(data["value"]))
                notify_state()
            else:
                logger.error("Received unnsupported event: {}", data)
    finally:
        USERS.remove(websocket)

async def ws_send(websocket, path):
    while True:
        message = await ws_queue.get()
        await asyncio.wait([user.send(message) for user in USERS])


def run_ws():
    # https://stackoverflow.com/questions/21141217/how-to-launch-win32-applications-in-separate-threads-in-python/22619084#22619084
    # https://www.reddit.com/r/learnpython/comments/mwt4qi/pywintypescom_error_2147417842_the_application/
    pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
    asyncio.set_event_loop(asyncio.new_event_loop())
    global ws_queue
    ws_queue = asyncio.Queue()
    global loop
    loop = asyncio.get_event_loop()
    start_server = websockets.serve(ws_handler, config.prefs["WebSocket"]["interface"], config.prefs.getint("WebSocket", "port"), ping_interval=None)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

def start_http():
    http_daemon = threading.Thread(name="http_daemon", target=run_http)
    http_daemon.setDaemon(True)
    http_daemon.start()
    logger.info("Started HTTP server")

def restart_http():
    global http_server
    if http_server:
        http_server.shutdown()
        http_server = None
        refresh_status()
    start_http()
    time.sleep(0.5)
    refresh_status()

def start_ws():
    global ws_daemon
    ws_daemon = threading.Thread(name="ws_daemon", target=run_ws)
    ws_daemon.setDaemon(True)
    ws_daemon.start()
    logger.info("Started websocket server")

class Slideshow:
    def __init__(self, instance, blackwhite):
        self.instance = instance
        if self.instance is None:
            raise ValueError("PPT instance cannot be None")

        if self.instance.SlideShowWindows.Count == 0:
            raise ValueError("PPT instance has no slideshow windows")
        self.view = self.instance.SlideShowWindows[0].View

        if self.instance.ActivePresentation is None:
            raise ValueError("PPT instance has no  active presentation")
        self.presentation = self.instance.ActivePresentation

        self.blackwhite = blackwhite

        self.export_current_next()

    def unload(self):
        connect_ppt()

    def refresh(self):
        try:
            if self.instance is None:
                raise ValueError("PPT instance cannot be None")

            if self.instance.SlideShowWindows.Count == 0:
                raise ValueError("PPT instance has no slideshow windows")
            self.view = self.instance.SlideShowWindows[0].View

            if self.instance.ActivePresentation is None:
                raise ValueError("PPT instance has no  active presentation")
        except:
            self.unload()

    def total_slides(self):
        try:
            self.refresh()
            return len(self.presentation.Slides)
        except (ValueError, pywintypes.com_error):
            self.unload()

    def current_slide(self):
        try:
            self.refresh()
            return self.view.CurrentShowPosition
        except (ValueError, pywintypes.com_error):
            self.unload()

    def visible(self):
        try:
            self.refresh()
            return self.view.State
        except (ValueError, pywintypes.com_error):
            self.unload()

    def prev(self):
        try:
            self.refresh()
            self.view.Previous()
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def next(self):
        try:
            self.refresh()
            self.view.Next()
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def first(self):
        try:
            self.refresh()
            self.view.First()
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()
                
    def last(self):
        try:
            self.refresh()
            self.view.Last()
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def goto(self, slide):
        try:
            self.refresh()
            if slide <= self.total_slides():
                self.view.GotoSlide(slide)
            else:
                self.last()
                self.next()
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def black(self):
        try:
            self.refresh()
            if self.blackwhite == "both" and self.view.State == 4:
                self.view.state = 1
            else:
                self.view.State = 3
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def white(self):
        try:
            self.refresh()
            if self.blackwhite == "both" and self.view.State == 3:
                self.view.state = 1
            else:
                self.view.State = 4
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def normal(self):
        try:
            self.refresh()
            self.view.State = 1
            self.export_current_next()
        except (ValueError, pywintypes.com_error):
            self.unload()

    def name(self):
        try:
            self.refresh()
            return self.presentation.Name
        except (ValueError, pywintypes.com_error):
            self.unload()


    def export_current_next(self):
        self.export(self.current_slide())
        self.export(self.current_slide() + 1)
        self.export(self.current_slide() + 2)

    def export(self, slide):
        destination = config.prefs["Main"]["cache"] + "\\" + self.name() + "\\" + str(slide) + ".jpg"
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        if not os.path.exists(destination) or time.time() - os.path.getmtime(destination) > config.prefs.getint("Main", "cache_timeout"):
            if slide <= self.total_slides():
                attempts = 0
                while attempts < 3:
                    try:
                        self.presentation.Slides(slide).Export(destination, config.prefs["Main"]["cache_format"])
                        break
                    except:
                        pass
                    attempts += 1
            elif slide == self.total_slides() + 1:
                try:
                    shutil.copyfileobj(open(os.path.dirname(os.path.realpath(__file__)) + r'''\static\black.jpg''', 'rb'), open(destination, 'wb'))
                except Exception as e:
                    logger.warning("Failed to copy black slide: " + str(e))
            else:
                pass

    def export_all(self):
        for i in range(1, self.total_slides()):
            self.export(i)

def get_ppt_instance():
    instance = win32com.client.Dispatch('Powerpoint.Application')
    if instance is None or instance.SlideShowWindows.Count == 0:
        return None
    return instance

def get_current_slideshow():
    return current_slideshow

def refresh_interval():
    while getattr(refresh_daemon, "do_run", True):
        current_slideshow.refresh()
        notify_state()
        refresh_status()
        time.sleep(0.5)

def refresh_status():
    if interface_root is not None and interface_root.state == "normal":
        logger.debug("Refreshing UI")
        if status_label is not None:
            status_label.config(text="PowerPoint status: " + ("not " if not STATE["connected"] else "") +  "connected")
        if http_label is not None:
            http_label.config(text="HTTP server: " + ("not " if http_server is None else "") +  "running")
            #ws_label.config(text="WebSocket server: " + ("not " if ws_daemon is not None or not ws_daemon.is_alive() else "") +  "running")
        if reset_ppt_button is not None:
            reset_ppt_button.config(state = tk.DISABLED if not STATE["connected"] else tk.NORMAL)

def connect_ppt():
    global STATE
    global refresh_daemon
    if STATE["connected"] == 1:
        logger.info("Disconnected from PowerPoint instance")
        icon.notify("Disconnected from PowerPoint instance")
        if reset_ppt_button is not None:
            reset_ppt_button.config(state = tk.DISABLED)
        refresh_daemon.do_run = False
        STATE = copy(STATE_DEFAULT)
        if icon is not None:
            refresh_menu()
        refresh_status()
        logger.debug("State is now " + str(STATE))
    while True:
        try:
            instance = get_ppt_instance()
            global current_slideshow
            current_slideshow = Slideshow(instance, config.prefs["Main"]["blackwhite"])
            STATE["connected"] = 1
            STATE["current"] = current_slideshow.current_slide()
            STATE["total"] = current_slideshow.total_slides()
            icon.notify("Connected to PowerPoint instance")
            if icon is not None:
                refresh_menu()
            refresh_status()
            logger.info("Connected to PowerPoint instance")
            refresh_daemon = threading.Thread(name="refresh_daemon", target=refresh_interval)
            refresh_daemon.setDaemon(True)
            refresh_daemon.start()
            break
        except ValueError as e:
            current_slideshow = None
            pass
        time.sleep(1)

def start(_=None):
    start_http()
    start_ws()
    connect_ppt()

def on_closing():
    global status_label
    global http_label
    global ws_label
    global interface_thread
    status_label = None
    http_label = None
    ws_label = None
    logger.debug("Destroying interface root")
    interface_root.destroy()
    logger.debug("Destroying interface thread")
    interface_thread.root.quit()
    interface_thread = None
    
def open_settings(_=None):
    global interface_root
    global interface_thread
    interface_root = tk.Tk()
    interface_root.protocol("WM_DELETE_WINDOW", on_closing)
    interface_root.iconphoto(False, tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + r'''\static\icons\ppt.png'''))
    interface_root.geometry("600x300+300+300")
    app = Interface(interface_root)
    interface_thread = threading.Thread(target=interface_root.mainloop())
    interface_thread.setDaemon(True)
    interface_thread.start()

def null_action():
    pass

def save_settings():
    pass

class Interface(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        global status_label
        global http_label
        global ws_label
        global reset_ppt_button
        self.parent.title("ppt-control")
        self.style = ttk.Style()
        #self.style.theme_use("default")
        self.focus_force()

        self.pack(fill=tk.BOTH, expand=1)

        quitButton = ttk.Button(self, text="Cancel", command=interface_root.destroy)
        quitButton.place(x=480, y=280)

        save_button = ttk.Button(self, text="OK", command=save_settings)
        save_button.place(x=400, y=280)

        reset_ppt_button = ttk.Button(self, text="Reconnect", command=connect_ppt)
        reset_ppt_button.config(state = tk.DISABLED)
        reset_ppt_button.place(x=300, y=10)

        reset_http_button = ttk.Button(self, text="Restart", command=restart_http)
        reset_http_button.place(x=300, y=30)

        #reset_ws_button = ttk.Button(self, text="Restart", command=null_action)
        #reset_ws_button.place(x=300, y=50)

        status_label = ttk.Label(self)
        status_label.place(x=10,y=10)

        http_label = ttk.Label(self)
        http_label.place(x=10,y=30)

        ws_label = ttk.Label(self)
        ws_label.place(x=10,y=50)

        refresh_status()
        
        
def exit_action(icon):
    logger.debug("User requested shutdown")
    icon.visible = False
    icon.stop()

def refresh_menu():
    icon.menu = (pystray.MenuItem("Status: " + "dis"*(not STATE["connected"]) + "connected", lambda: null_action(), enabled=False),
            pystray.MenuItem("Stop", lambda: exit_action(icon)),
            pystray.MenuItem("Settings", lambda: open_settings(), enabled=False)
            )

def show_icon():
    global icon
    logger.debug("Starting system tray icon")
    icon = pystray.Icon("ppt-control")
    icon.icon = Image.open(os.path.dirname(os.path.realpath(__file__)) + r'''\static\icons\ppt.ico''')
    icon.title = "ppt-control"
    refresh_menu()
    icon.visible = True
    icon.run(setup=start)

def start_interface():
    global logger

    # Load config
    config.prefs = config.loadconf(CONFIG_FILE)

    # Set up logging
    if config.prefs["Main"]["logging"] == "debug":
        log_level = logging.DEBUG
    elif config.prefs["Main"]["logging"] == "info":
        log_level = logging.CRITICAL
    else:
        log_level = logging.WARNING
    log_level = logging.DEBUG

    log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-7.7s]  %(message)s")
    logger = logging.getLogger("ppt-control")
    logger.setLevel(log_level)
    logger.propagate = False

    file_handler = logging.FileHandler("{0}/{1}".format(os.getenv("APPDATA"), LOGFILE))
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)

    #logging.getLogger("asyncio").setLevel(logging.ERROR)
    #logging.getLogger("asyncio.coroutines").setLevel(logging.ERROR)
    logging.getLogger("websockets.server").setLevel(logging.ERROR)
    #logging.getLogger("websockets.protocol").setLevel(logging.ERROR)


    logger.debug("Finished setting up config and logging")

    # Start systray icon and server
    show_icon()
    sys.exit(0)

if __name__ == "__main__":
    start_interface()
