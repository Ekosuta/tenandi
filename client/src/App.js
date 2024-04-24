import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Lesson from './pages/Lesson'
import Unit from './pages/Unit'
import Units from './pages/Units'
import Main from './pages/Main'

function App() {
  return (
    <div>
      <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Main />}/>
        <Route path='/units' exact element={<Units />}/>
        <Route path='/units/:unitId' exact element={<Unit />}/>
        <Route path='/units/:unitId/:lessonId' exact element={<Lesson />}/>
      </Routes>
    </Router>
    </div>
  );
}

export default App;
