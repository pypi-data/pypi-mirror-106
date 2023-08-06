const COOKIENAME = "settings";
const COOKIEEXP = 365;

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return 0;
}

function saveSettings() {
    console.log("Saving settings")
    settingsString = JSON.stringify({showcurrent: show_current.checked, shownext: show_next.checked, enable_shortcuts: shortcuts.checked});
    setCookie(COOKIENAME, settingsString, COOKIEEXP);
}

function initSettings() {
    if (getCookie(COOKIENAME) == 0) {
        if (window.obssstudio) {
                shortcuts.checked = False;
                show_current.checked = False;
        }
        saveSettings()
    } else {
        cookie = JSON.parse(getCookie(COOKIENAME));
        show_current.checked = cookie.showcurrent;
        show_next.checked = cookie.shownext;
        shortcuts.checked = cookie.enable_shortcuts;
        sync_current();
        sync_next();
    }

}

