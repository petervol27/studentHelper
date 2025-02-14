import axios from 'axios';
const HOST = 'http://127.0.0.1:8000';

// ---------- AUTH ---------------
export const login = async (username, password) => {
  const credentials = { username: username, password: password };
  const response = await axios.get(`${HOST}/students/login`, credentials);
  return response.data;
};

export const register = async (username, password) => {
  const credentials = { username: username, password: password };
  const response = await axios.post(`${HOST}/students/register`, credentials);
  return response.data;
};

// ---------- EXERCISES ---------------
