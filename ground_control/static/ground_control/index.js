
const msgInput = document.querySelector('#satellite-number-input');
const submit = document.querySelector('#satellite-number-submit');

msgInput.focus();

msgInput.onkeyup = (evt) => {
    if (evt.keyCode === 13) { //enter, return
        submit.click();
    }
};

submit.onclick = () => {
    const numberOfSatellites = msgInput.value;
    if (isNaN(parseInt(numberOfSatellites)))  {
        window.alert('Please, enter a valid integer!');
        return;
    }
    window.location.pathname = '/ground_control/earth/' + numberOfSatellites + '/';
};
