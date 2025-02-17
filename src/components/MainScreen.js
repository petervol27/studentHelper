import { useContext, useState } from 'react';
import ExerciseScreen from './ExerciseScreen';
import UserContext from '../context/UserContext';
import { useNavigate } from 'react-router-dom';
import { getQuestions } from '../api';

const MainScreen = () => {
  const navigate = useNavigate();
  const [difficulty, setDifficulty] = useState(null);
  const { user, setUser } = useContext(UserContext);
  const handleLogout = () => {
    alert('Thank you for using our service');
    setUser(false);
    navigate('/');
  };
  const renderExercise = (level) => {
    getQuestions(level);
  };
  return (
    <>
      <div className="container text-center">
        <div className="container position-relative text-center mt-3">
          <h1 className="mb-0">Welcome to Student Helper </h1>
          <button
            className="btn btn-primary position-absolute top-0 end-0 "
            onClick={() => handleLogout()}
          >
            Logout
          </button>
        </div>
        <p className="text-secondary">
          Your coding exercises to pass your next interview!
        </p>
        <h3 className="mb-3">Hello {user}</h3>
        <div className="container w-50 mx-auto">
          <h3>Choose Difficulty:</h3>
          <div className="d-flex justify-content-center align-items-center gap-3 mb-3">
            <button
              className="btn btn-success"
              value="beginner"
              onClick={(e) => {
                setDifficulty(e.target.value);
                renderExercise(e.target.value);
              }}
            >
              Beginner
            </button>
            <button
              className="btn btn-warning"
              value="intermidiate"
              onClick={(e) => {
                setDifficulty(e.target.value);
                renderExercise(e.target.value);
              }}
            >
              Intermidiate
            </button>
            <button
              className="btn btn-danger"
              value="professional"
              onClick={(e) => {
                setDifficulty(e.target.value);
                renderExercise(e.target.value);
              }}
            >
              Professional
            </button>
          </div>
        </div>
      </div>
      {difficulty && <ExerciseScreen />}
    </>
  );
};

export default MainScreen;
