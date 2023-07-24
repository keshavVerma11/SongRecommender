import React, { useState } from 'react';
import axios from 'axios';
import './TextBox.css';

const TextBox = () => {
  const [inputText, setInputText] = useState('');
  const [responseData, setResponseData] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSubmit = () => {
    axios
      .post('http://localhost:5000/textbox/submit', { text: inputText })
      .then((response) => {
        setResponseData(response.data.response);;
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div>
      <input
        type="text"
        value={inputText}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        placeholder="Enter text..."
        className="custom-textbox"
      />
      <button onClick={handleSubmit} className="custom-button">Enter</button>
      <p>{responseData}</p> {}
    </div>
  );
};

export default TextBox;