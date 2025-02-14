import React from 'react';

const ExerciseScreen = () => {
  return (
    <div className="container text-center w-50 mx-auto">
      <h4>--Question--</h4>
      <form>
        <textarea className="form-control" rows={10}></textarea>
        <input type="submit" className="btn btn-primary mt-3"></input>
      </form>
    </div>
  );
};

export default ExerciseScreen;
