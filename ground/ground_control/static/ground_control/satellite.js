const roomName = JSON.parse(document.getElementById('satellite_name').textContent);
const numberOfSatellites = JSON.parse(document.getElementById('number_of_satellites').textContent);

const msgInput = document.querySelector('#chat-message-input');
const submit = document.querySelector('#chat-message-submit');
const earthLog = document.querySelector('#earth-log');

msgInput.value = 
`{
    "task": [
        {
            "name": "fotos",
            "pay_off": 10,
            "resources": [1, 5] 
        },
        {
            "name": "mantenimiento",
            "pay_off": 1,
            "resources": [1, 2] 
        },
        {
            "name": "pruebas",
            "pay_off": 1,
            "resources": [5, 6] 
        },
        {
            "name": "fsck",
            "pay_off": 0.1,
            "resources": [1, 6] 
        }
    ]
}`;

const earthSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/ground_control/'
    + roomName
    + '/'
    + numberOfSatellites
    + '/'
);

for (let i = 1; i < parseInt(numberOfSatellites) + 1; i++) {
    new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/ground_control/'
        + 'satellite_'
        + i
        + '/'
    )
    .onmessage = (evt) => {
        const data = JSON.parse(evt.data);
        earthLog.value += (data.message + '\n');
    };
}

earthSocket.onclose = () => {
    console.error('Chat socket closed unexpectedly');
};

msgInput.focus();
// msgInput.onkeyup = (evt) => {
//     if (evt.keyCode === 13) {  // enter, return
//         submit.click();
//     }
// };

submit.onclick = () => {
    const message = msgInput.value;
    earthSocket.send(JSON.stringify({
        'message': message
    }));
    msgInput.value = '';
};
