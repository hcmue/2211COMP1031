import { Route, Routes, Link } from 'react-router-dom';
import { About } from './About';
import { ToDoList } from './TodoList';
import { Counter } from './Counter';

function App() {
  return (
    <div className="App">
      <header style={{ border: '1px solid blue', padding: 5 }}>
        <a href='/about'>About</a>
        <a href='/todos'>Todos</a>
        <a href='/counter'>COUNTER</a>
      </header>
      <Routes>
        <Route path='/' exact element={<About />} />
        <Route path="about" element={<About />} />
        <Route path="todos" element={<ToDoList />} />
        <Route path="counter" element={<Counter />} />
      </Routes>
      <h2>HOME</h2>
    </div>
  );
}

export default App;
