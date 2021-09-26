import React, { useState } from 'react';
import Box from '@mui/material/Box';
import { v4 as uuidv4 } from 'uuid'; 
import Task from './Task';
import TaskForm from './TaskForm';
import Button from '@mui/material/Button';
import { parseResources } from '../utils';
import axios from 'axios';


export default function TaskList() {

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
        await axios.post(endpoint, {"tasks": sendList});
        setTasks([]);
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
                <TaskForm addTask={addTask} />
                <div>
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
                </div>
                <Button 
                    variant="outlined"
                    onClick={sendToSatellite}
                >
                    Send to Satellites
                </Button>
            </Box>
        </div>
    );
}