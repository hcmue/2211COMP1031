import React from 'react';
import { Routes, Route, BrowserRouter, Link } from 'react-router-dom';
import { Counter } from './components/Counter';
import { About } from './components/About';
import { Todo } from './components/Todo';
import { HomePage } from './components/Home';
import { MyContextProvider } from './contexts/MyContext';
import './App.css';


function App() {
  return (
    <div className="App">
      <MyContextProvider>
        <BrowserRouter>
          <nav>
            <Link to='/' className='mylink'>Home</Link>
            <a href='/counter' className='mylink'>Counter</a>
            <a href='/todos' className='mylink'>TODOs</a>
            <Link to='/about' className='mylink'>About</Link>
          </nav>
          <Routes>
            <Route exact path='/' element={<HomePage />} />
            <Route exact path='/counter' element={<Counter />} />
            <Route exact path='/todos' element={<Todo />} />
            <Route exact path='/about' element={<About />} />
          </Routes>
        </BrowserRouter>
      </MyContextProvider>
    </div >
  );
}

export default App;
