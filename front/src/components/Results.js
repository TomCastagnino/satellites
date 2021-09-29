import { Card, CardContent, List, ListItem, ListItemText, Typography } from '@mui/material';
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
        marginLeft: 0,
        padding: 25
    }
}));

export default function Results(props) {

    const classes = useStyles();

    return (
        <Card className={classes.resultsPaper}>
            {props.results.length !== 0 &&
            props.results.hasOwnProperty('message') 
            && props.results['message'].map(arr => {
                return (
                    <CardContent>
                        {
                            arr.map((result, ix) => {
                                const time = new Date(Date.parse(result['date_added']))
                                const day = time.getDate();
                                const month = time.getMonth() + 1;
                                const year = time.getFullYear();
                                const strTime = `${time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds()} ${day}/${month}/${year}`
                                return (
                                <Typography color="text.secondary" key={ix}>
                                    <Typography><strong>{result['name']}</strong></Typography>
                                    <List>
                                        <ListItem><ListItemText>Assigned to: {result['assigned_to']}</ListItemText></ListItem>
                                        <ListItem><ListItemText>Date: {strTime}</ListItemText></ListItem>
                                        <ListItem><ListItemText>Completed: {result['completed'] ? 'True' : 'False'}</ListItemText></ListItem>
                                    </List>
                                </Typography>
                                );
                            })
                        }
                    </CardContent>
                    );
            })}
        </Card>
    );
}