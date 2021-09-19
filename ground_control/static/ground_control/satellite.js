const roomName = JSON.parse(document.getElementById('satellite_name').textContent);
console.log(roomName);
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/ground_control/'
    + roomName
    + '/'
);

const satelliteSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/ground_control/'
    + 'satellite1'
    + '/'
)

const satelliteSocket2 = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/ground_control/'
    + 'satellite2'
    + '/'
)

// chatSocket.onmessage = function(e) {
//     const data = JSON.parse(e.data);
//     document.querySelector('#earth-log').value += (data.message + '\n');
// };

satelliteSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#earth-log').value += (data.message + '\n');
};

satelliteSocket2.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#earth-log').value += (data.message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};