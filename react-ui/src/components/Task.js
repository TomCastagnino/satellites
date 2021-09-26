import * as React from 'react';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import { Stack } from '@mui/material';


export default function Task(props) {

    const { id, task, deleteTask } = props;

    const handleDelete = evt => {
        deleteTask(id);
    };

    return (    
            <Stack
                direction="row"
                alignItems="center"
                spacing={2}
            >
                <div>{task.name}</div>
                <div>{task.payoff}</div>
                <div>{task.resources}</div>
                <div><IconButton 
                    aria-label="delete"
                    onClick={handleDelete}
                >
                    <DeleteIcon />
                </IconButton>
                </div>
            </Stack>
    )

}
