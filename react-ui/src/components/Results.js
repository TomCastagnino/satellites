import { Paper } from '@mui/material';
import * as React from 'react';
import { makeStyles } from '@mui/styles';


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        margin: 0
    },
    resultsPaper: {
        // display: 'flex',
        widht: '50%',
        alignItems: 'center',
        justifyContent: 'center',
        margin: 50,
        padding: 25
    }
}));

export default function Results(props) {

    const classes = useStyles();

    return (
        <Paper className={classes.resultsPaper}>
            {props.results.length !== 0 &&
            props.results.hasOwnProperty('message') 
            && props.results['message'].map(arr => {
                return arr.map((result, ix) => {
                    return (
                    <div key={ix}>
                        {result.name}
                        {result['assigned_to']}
                        {result['date_added']}
                        {result['completed']}
                    </div>
                    );
                })
            })}
        </Paper>
    );
}