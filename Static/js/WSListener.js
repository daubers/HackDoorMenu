/**
 * Created by Matthew on 08/06/2014.
 */

function setupWebSocket(path, onmessage, onopen, onclose, onerror){
    /**
     * Returns a websocket object connected to path
     * Sets up the on* calls as callbacks
     */
    try {
        var socket = new WebSocket(path);
        socket.onopen = function () {
            onopen();
        };
        socket.onclose = function () {
            onclose();
        };
        socket.onmessage = function (msg) {
            onmessage(msg);
        };
        socket.onerror = function () {
            onerror();
        };
    } catch(exception) {
        return exception;
    }
        return socket;
}