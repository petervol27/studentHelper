import axios from 'axios';
const HOST = 'http://127.0.0.1:8000';

// ---------- AUTH ---------------
export const login = async (username, password) => {
  const credentials = { username: username, password: password };
  try {
    const response = await axios.post(`${HOST}/students/login/`, credentials);
    return response.data;
  } catch (error) {
    return error;
  }
};

export const register = async (username, password) => {
  const credentials = { username: username, password: password };
  try {
    const response = await axios.post(
      `${HOST}/students/register/`,
      credentials
    );
    return response.data;
  } catch (error) {
    return error;
  }
};

// ---------- EXERCISES ---------------
export const getQuestions = async (difficulty) => {
  const response = await axios.post(`${HOST}/questions/list/`, {
    difficulty: difficulty,
  });
  console.log(response.data);
};
