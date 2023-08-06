var DEFAULT_TITLE = "ppt-control"
var preloaded = false;
var preload = [];

var prev = document.querySelector('#prev'),
    next = document.querySelector('#next'),
    first = document.querySelector('#first'),
    last = document.querySelector('#last'),
    black = document.querySelector('#black'),
    white = document.querySelector('#white'),
    slide_label = document.querySelector('#slide_label'),
    current = document.querySelector('#current'),
    total = document.querySelector('#total'),
    status_text = document.querySelector('.status_text'),
    current_img = document.querySelector('#current_img'),
    next_img = document.querySelector('#next_img'),
    current_div = document.querySelector('#current_div'),
    next_div = document.querySelector('#next_div'),
    controls_container = document.querySelector('#controls_container'),
    controls_container_inner = document.querySelector('#controls_container_inner'),
    show_current = document.querySelector('#show_current'),
    show_next = document.querySelector('#show_next'),
    shortcuts = document.querySelector('#shortcuts');


function startWebsocket() {
    console.log("Attempting to connect")
    ws = new WebSocket("ws://" + window.location.host + ":5678/");
    ws.onmessage = receive_message;
    ws.onclose = function(){
        ws = null;
        setTimeout(function(){websocket = startWebsocket()}, 1000);
    }
    if (ws.readyState !== WebSocket.OPEN) {
      disconnect()
    }
    return ws;
}

var websocket = startWebsocket();

prev.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'prev'}));
}

next.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'next'}));
}

first.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'first'}));
}

last.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'last'}));
}

black.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'black'}));
}

white.onclick = function (event) {
    websocket.send(JSON.stringify({action: 'white'}));
}

current.onblur = function (event) {
    websocket.send(JSON.stringify({action: 'goto', value: current.value}));
}

current.addEventListener('keyup',function(e){
    if (e.which == 13) this.blur();
});

current_img.onclick = function (event) {
	next.click()
}

next_img.onclick = function (event) {
	next.click()
}


function sync_current() {
    if (show_current.checked) {
        current_div.style.display = "block";
        slide_label.style.display = "none";
        next_div.style.width = "25%";
    } else {
        current_div.style.display = "none";
        slide_label.style.display = "inline";
        next_div.style.width = "calc(100% - 20px)";
    }
    set_control_width();
    saveSettings();
}
show_current.onclick = sync_current;

function sync_next() {
    if (show_next.checked) {
        next_div.style.display = "block";
        current_div.style.width = "70%";
    } else {
        next_div.style.display = "none";
        current_div.style.width = "calc(100% - 20px)";
    }
    set_control_width();
    saveSettings();
}
show_next.onclick = sync_next;

function sync_shortcuts() {
  saveSettings();
}
shortcuts.onclick = sync_shortcuts;

function set_control_width() {
	var width = window.innerWidth
	|| document.documentElement.clientWidth
	|| document.body.clientWidth;
    if (show_current.checked && show_next.checked && width > 800) {
        controls_container_inner.style.width = "70%"
    } else {
    	controls_container_inner.style.width = "100%"
    }
}


document.addEventListener('keydown', function (e) {
	if (shortcuts.checked) {
		switch (e.key) {
			case "Left":
			case "ArrowLeft":
			case "Up":
			case "ArrowUp":
			case "k":
			case "K":
				prev.click();
				break;
			case " ":
			case "Spacebar":
			case "Enter":
			case "Right":
			case "ArrowRight":
			case "Down":
			case "ArrowDown":
			case "j":
			case "J":
				next.click();
				break;
			case "b":
			case "B":
				black.click();
			case "w":
			case "W":
				white.click();
			default:
				return
		}
	}
});

function disconnect() {
  console.log("Disconnecting")
    document.title = DEFAULT_TITLE;
    current_img.src = "/black.jpg";
    next_img.src = "/black.jpg";
    status_text.textContent = "Disconnected";
    total.textContent = "?";
    current.value = "";
}

function receive_message(event) {
    data = JSON.parse(event.data);
    switch (data.type) {
        case 'state':
            if (data.connected == "0" || data.connected == 0) {
            	disconnect();
            	break;
            } else {
              status_text.textContent = "Connected";
            }
            var d = new Date;
            if (show_current.checked) {
              switch (data.visible) {
                  case 3:
                      current_img.src = "/black.jpg";
                      break;
                  case 4:
                      current_img.src = "/white.jpg";
                      break;
                  default:
                      current_img.src = "/cache/" + data.current + ".jpg?t=" + d.getTime();
                      //current_img.src = "/cache/" + data.current + ".jpg";
                      break;
              }
            }
            if (data.current == data.total + 1) { 
                next_img.src = "/cache/" + (data.total + 1) + ".jpg?t=" + d.getTime();
                //next_img.src = "/cache/" + (data.total + 1) + ".jpg";
            } else {
                next_img.src = "/cache/" + (data.current + 1) + ".jpg?t=" + d.getTime();
                //next_img.src = "/cache/" + (data.current + 1) + ".jpg";
            }

            if (document.activeElement != current) {
            	current.value = data.current;
            }
            total.textContent = data.total;
            document.title = data.name;
            break;
        default:
            console.error(
                "Unsupported event", data);
    }
	if (preloaded == false && ! isNaN(total.textContent)) {
		image = document.getElementById("preload_img");
		for (let i=1; i<=Number(total.textContent); i++) {
			image.src = "/cache/" + i + ".jpg";
			preload.push(image);
		}
		preloaded = true;
	}

};
