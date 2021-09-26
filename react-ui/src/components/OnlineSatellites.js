import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Paper } from '@mui/material';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        margin: 0
    },
    onlineSatellitesPaper: {
        // display: 'flex',
        widht: '50%',
        alignItems: 'center',
        justifyContent: 'center',
        margin: 50,
        padding: 25
    }
}));

export default function OnlineSatellites() {
    
    const classes = useStyles();

    const [ satellites, setSatellites ] = useState([]);

    const getSatellites = async () => {
        const endpoint = 'http://127.0.0.1:8000/api/online_satellites/';
        const response = await axios.get(endpoint);
        setSatellites(response['data']['message']);
    };

    useEffect(() => {
       getSatellites(); 
    }, []);

    return (
        <Paper className={classes.onlineSatellitesPaper}>
            Online Satellites:
            {satellites.length}

            [ {satellites} ]
        </Paper>
    );
}