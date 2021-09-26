import * as React from 'react';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';


export default function Task(props) {

    const { id, task, deleteTask } = props;

    const handleDelete = evt => {
        deleteTask(id);
    };

    return (    
        <div>
            <Box
                sx={{
                    display: 'flex',
                    alignItems: 'center',
                    width: 'fit-content',
                    border: (theme) => `1px solid ${theme.palette.divider}`,
                    borderRadius: 1,
                    bgcolor: 'background.paper',
                    color: 'text.secondary',
                    '& svg': {
                    m: 1.5,
                    },
                    '& hr': {
                    mx: 0.5,
                    },
                }}
            >
                <div>{task.name}</div>
                <Divider orientation="vertical" flexItem />
                <div>{task.payoff}</div>
                <Divider orientation="vertical" flexItem />
                <div>{task.resources}</div>
                <Divider orientation="vertical" flexItem />
                <IconButton 
                    aria-label="delete"
                    onClick={handleDelete}
                >
                    <DeleteIcon />
                </IconButton>
            </Box>
        </div>
    )

}
