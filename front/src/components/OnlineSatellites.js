import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, CardContent, Typography } from '@mui/material';
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
        marginLeft: 0,
        padding: 25
    }
}));

export default function OnlineSatellites() {
    
    const classes = useStyles();

    const [ satellites, setSatellites ] = useState([]);

    const getSatellites = async () => {
        const api_url = process.env.REACT_APP_GROUND_API_HOST ? process.env.REACT_APP_GROUND_API_HOST : 'http://127.0.0.1:8000';
        const endpoint = api_url + '/api/online_satellites/';
        const response = await axios.get(endpoint);
        setSatellites(response['data']);
    };

    useEffect(() => {
       getSatellites(); 
    }, []);

    return (
        <Card className={classes.onlineSatellitesPaper}>
            <CardContent>
                <Typography variant="h5" color="text.secondary">
                    Number of satellites online: {satellites.length} 
                    <br/>
                </Typography>
                <Typography variant="body2" color="text.secondary" style={{marginTop: 30}}>
                    {satellites.map((object, i) => <div>{object.name}</div>)}
                </Typography>
            </CardContent>
        </Card>
    );
}