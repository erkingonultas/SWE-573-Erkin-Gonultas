import React, { createContext, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token') || null);

  const register = async (email, username, password) => {
    try {
      const response = await axios.post('http://localhost:8080/auth/register', { email, username, password });
      const token = response.data.token;
      setToken(token);
      localStorage.setItem('token', token);
      console.log("Successful");
    } catch (error) {
      console.log(error);
    }
    
    
  };

  const login = async (email, password) => {
    const response = await axios.post('http://localhost:8080/auth/login', { email, password });
    const token = response.data.token;
    setToken(token);
    localStorage.setItem('token', token);
  };

  const logout = () => {
    setToken(null);
    localStorage.removeItem('token');
  };

  return (
    <AuthContext.Provider value={{ token, register, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
