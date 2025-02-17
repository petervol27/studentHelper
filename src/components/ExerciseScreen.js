import React, { useEffect, useState } from 'react';
import { submitCode } from '../api';

const ExerciseScreen = ({ questions }) => {
  const [currentQuestionNum, setCurrentQuestionNum] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(questions[0]);
  const [code, setCode] = useState('');
  const [checkedAnswer, setCheckedAnswer] = useState('');

  // ✅ Properly update `currentQuestion` when `currentQuestionNum` changes
  useEffect(() => {
    if (currentQuestionNum < questions.length) {
      setCurrentQuestion(questions[currentQuestionNum]);
      setCheckedAnswer(''); // Reset feedback
      setCode(''); // Reset textarea for new question
    }
  }, [currentQuestionNum, questions]);

  const handleNextQuestion = () => {
    if (currentQuestionNum < questions.length - 1) {
      setCurrentQuestionNum((prev) => prev + 1); // Update state safely
    }
  };

  const handleOnSubmit = (e) => {
    e.preventDefault();

    // 🚨 Validate first line starts with `def`
    const firstLine = code.split('\n')[0].trim();
    const firstWord = firstLine.split(' ')[0];

    if (firstWord !== 'def') {
      setCheckedAnswer(
        '❌ Your code must start with `def function_name()` on the first line.'
      );
      return;
    }

    submitCode(code, currentQuestion.id).then((res) => {
      console.log(res);
      if (res.code) {
        setCheckedAnswer(res.response.data.result);
        return;
      }
      setCheckedAnswer(res.result);
    });
  };

  return (
    <div className="container text-center w-50 mx-auto">
      <h4 className="lead">{currentQuestion.description}</h4>
      <h3 className="lead">Expected Output: {currentQuestion.result}</h3>
      <form onSubmit={handleOnSubmit}>
        <textarea
          className="form-control"
          rows={10}
          value={code} // Keep textarea controlled
          onChange={(e) => setCode(e.target.value)}
        ></textarea>
        <p className="text-dark mt-2">{checkedAnswer}</p>
        <input type="submit" className="btn btn-primary mt-3"></input>
      </form>

      {checkedAnswer === '✅ Correct!' &&
        currentQuestionNum < questions.length - 1 && (
          <button className="btn btn-success mt-3" onClick={handleNextQuestion}>
            Next Question
          </button>
        )}
    </div>
  );
};

export default ExerciseScreen;
