import './App.css';
import NavBar from './components/NavBar';
import TaskList from './components/TaskList';
import OnlineSatellites from './components/OnlineSatellites';
import { useState } from 'react';
import Results from './components/Results';
import { Grid } from '@mui/material';


function App() {

  const [results, setResults ] = useState([]);

  return (
    <div className="App">
      <NavBar />
        <Grid container spacing={0}>
          <Grid item xs={8}>
            <TaskList setResults={setResults} />
          </Grid>
        <Grid item xs={4}>
          <OnlineSatellites />
          <Results results={results} />
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
