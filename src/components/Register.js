import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { register } from '../api';
const Register = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const handleRegister = (e) => {
    e.preventDefault();
    register(username, password).then((res) => {
      if (res.error) {
        setError(res.error);
      } else {
        alert(res.success);
        navigate('/');
      }
    });
  };
  return (
    <div className="container">
      <form
        className="w-25 mx-auto border rounded mt-5 p-3 text-center"
        onSubmit={(e) => handleRegister(e)}
      >
        <h2 className="text-center">Register</h2>
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
          <input type="submit" className="btn btn-primary "></input>
        </div>
        <p className="text-danger">{error}</p>
      </form>
      <div className="text-center mt-3">
        <button
          className="btn btn-warning text-center"
          onClick={() => navigate('/')}
        >
          Already have an account?
        </button>
      </div>
    </div>
  );
};

export default Register;
