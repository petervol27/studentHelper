import React, { useState } from 'react';
import { Route, BrowserRouter, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import UserContext from './context/UserContext';
import MainScreen from './components/MainScreen';
const App = () => {
  const [user, setUser] = useState(true);
  return (
    <>
      <UserContext.Provider value={{ user, setUser }}>
        <BrowserRouter>
          <Routes>
            {!user && (
              <>
                <Route path="/" element={<Login />}></Route>
                <Route path="/register" element={<Register />}></Route>
              </>
            )}
            {user && <Route path="/main" element={<MainScreen />}></Route>}
          </Routes>
        </BrowserRouter>
      </UserContext.Provider>
    </>
  );
};

export default App;
