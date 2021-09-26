import React, { useState } from 'react';
import Box from '@mui/material/Box';
import { v4 as uuidv4 } from 'uuid'; 
import Task from './Task';
import TaskForm from './TaskForm';
import Button from '@mui/material/Button';
import { parseResources } from '../utils';
import axios from 'axios';
import { Paper } from '@mui/material';
import { Grid } from '@mui/material';
import { makeStyles } from '@mui/styles';



const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        margin: 0
    },
    taskListPaper: {
        // display: 'flex',
        widht: '50%',
        alignItems: 'center',
        justifyContent: 'center',
        margin: 50,
        padding: 25
    }
}));

export default function TaskList(props) {

    const classes = useStyles();

    const [ tasks, setTasks ] = useState([]);

    const addTask = task => {
        setTasks((prevState) => {
            task['id'] = uuidv4();
            return [...prevState, task]  
        });
    };

    const deleteTask = id => {
        const newTasks = tasks.filter(task => task.id !== id);
        setTasks(newTasks);
    };

    const sendToSatellite = async () => {
        const sendList = [];
        for (let task of tasks) {
            const resources = parseResources(task['resources']);
            const temp = {
                "name": task['name'],
                "pay_off": parseFloat(task['payoff']),
                "resources": resources
            }
            sendList.push(temp);
        }
        const endpoint = 'http://127.0.0.1:8000/api/start_button/';
        const response = await axios.post(endpoint, {"tasks": sendList});
        setTasks([]);
        props.setResults(response['data']);
    };

    return (
        <div>
            <Box
                component="form"
                sx={{
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <Paper elevation={3} className={classes.taskListPaper}>
                <TaskForm addTask={addTask} />
                <div>
                    <Grid flex={1} container direction="column" justifyContent="center" alignItems="center">
                        <Grid item >
                    {tasks.map((task, ix) => {
                        return (
                            <Task
                                task={task}
                                id={task.id}
                                key={ix}
                                deleteTask={deleteTask}
                            />
                        );
                    })}
                    </Grid>
                    </Grid>
                </div>
                <Button 
                    variant="outlined"
                    onClick={sendToSatellite}
                    disabled={tasks.length === 0}
                >
                    Send to Satellites
                </Button>
                </Paper>
            </Box>
        </div>
    );
}