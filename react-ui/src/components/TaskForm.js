import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';


export default function TaskForm(props) {

    const { addTask } = props;

    const [ task, setTask ] = React.useState({});

    const manageTask = evt => {
        setTask((prevState) => {
            return {
                ...prevState,
                [evt.target.id]: evt.target.value
            }
        });
    }

    const handleSubmit = evt => {
        addTask({...task});
        setTask({})
    };

    return (
        <div>
            <TextField
                id="name"
                label="Name"
                value={task['name'] || ''}
                onChange={manageTask}
            />
            <TextField
                id="payoff"
                label="Payoff"
                value={task['payoff'] || ''}
                onChange={manageTask}
            />
            <TextField
                id="resources"
                label="Resources"
                helperText="Comma separated resources"
                value={task['resources'] || ''}
                onChange={manageTask}
            />
            <Button 
                variant="outlined"
                onClick={handleSubmit}
            >
                Add Task
            </Button>
        </div>
    );
}