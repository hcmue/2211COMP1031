import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import { Login } from './components/Login';
import { HomePage } from './components/Home';
import { About } from './components/About';
import { MyContextProvider } from './contexts/MyContext';

function App() {
  return (
    <div className="App">
      <MyContextProvider>
        <BrowserRouter>
          <nav>
            <Link to='/about'>About</Link>
            <Link to='/login'>Login</Link>
            <Link to='/Home'>Home</Link>
          </nav>

          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
          </header>

          <Routes>
            <Route exact path='/' element={<HomePage />} />
            <Route exact path='/about' element={<About />} />
            <Route exact path='/home' element={<HomePage />} />
            <Route exact path='/login' element={<Login />} />
          </Routes>
        </BrowserRouter>
      </MyContextProvider>
    </div>
  );
}

export default App;
