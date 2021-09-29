import * as React from 'react';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import TextField from '@mui/material/TextField';
import { Grid, IconButton, Paper } from '@mui/material';


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

    const isReady = task => {
        return (
            task.hasOwnProperty('name') && task.name !== '' &&
            task.hasOwnProperty('payoff') && task.payoff !== '' &&
            task.hasOwnProperty('resources') && task.resources.length !== 0
        )
    }

    return (
        <Paper elevation={0}>
        <Grid flex={1} container direction="row" justifyContent="center" alignItems="center">
            <Grid item>
            <TextField
                id="name"
                label="Name"
                helperText="Task name"
                value={task['name'] || ''}
                onChange={manageTask}
            />
            </Grid>
            <Grid item>
            <TextField
                id="payoff"
                label="Payoff"
                helperText="Task value"
                value={task['payoff'] || ''}
                onChange={manageTask}
            />
            </Grid>
            <Grid item>
            <TextField
                id="resources"
                label="Resources"
                helperText="Comma separated resources"
                value={task['resources'] || ''}
                onChange={manageTask}
            />
            </Grid>
            <Grid item>
                <IconButton
                    onClick={handleSubmit}
                    disabled={!isReady(task)}
                >
                    <AddCircleOutlineIcon fontSize="large" />
                </IconButton>
            </Grid>
        </Grid>
        </Paper>
    );
}