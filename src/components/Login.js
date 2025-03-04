import { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserContext from '../context/UserContext';
import { login } from '../api';

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { setUser } = useContext(UserContext);
  const handleLogin = (e) => {
    e.preventDefault();
    login(username, password).then((res) => {
      console.log(res);
      if (res.refresh) {
        localStorage.setItem('token', res.refresh);
        localStorage.setItem('name', username);
        setUser(username);
        navigate('main');
      } else {
        setError(res.response.data.detail);
      }
    });
  };
  return (
    <div className="container">
      <form
        className="w-25 mx-auto border rounded mt-5 p-3 text-center"
        onSubmit={(e) => handleLogin(e)}
      >
        <h2 className="text-center">Please Login</h2>
        <label htmlFor="username">Username:</label>
        <input
          className="form-control "
          type="text"
          name="username"
          onChange={(e) => setUsername(e.target.value)}
        ></input>
        <label htmlFor="password">Password:</label>
        <input
          className="form-control "
          type="password"
          name="password"
          onChange={(e) => setPassword(e.target.value)}
        ></input>
        <div className="text-center mt-3">
          <input type="submit" className="btn btn-primary"></input>
        </div>
        <p className="text-danger">{error}</p>
      </form>
      <div className="text-center mt-3">
        <button
          className="btn btn-warning"
          onClick={() => navigate('register')}
        >
          Don't Have an Account?
        </button>
      </div>
    </div>
  );
};

export default Login;
