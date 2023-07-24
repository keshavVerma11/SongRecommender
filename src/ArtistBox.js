import React, { useState } from 'react';
import axios from 'axios';
import './TextBox.css';

const ArtistBox = () => {
    const [inputText, setInputText] = useState('');
    const [responseData, setResponseData] = useState('');
  
    const handleInputChange = (event) => {
      setInputText(event.target.value);
    };
  
    const handleSubmit = () => {
      axios
        .post('http://localhost:5000/artistbox/submit', { text: inputText })
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
        {responseData.length == 0 ? (
          ""
        ) : (
          <>
            <div className="image-container">
              <p>{"1: " + responseData[0][0] + ", By " + responseData[0][1]}</p>
              <img
                src={responseData[0][2]}
                alt="Image"
                className="custom-image"
              />
              <p>{"2: " + responseData[1][0] + ", By " + responseData[1][1]}</p>
              <img
                src={responseData[1][2]}
                alt="Image"
                className="custom-image"
              />
              <p>{"3: " + responseData[2][0] + ", By " + responseData[2][1]}</p>
              <img
                src={responseData[2][2]}
                alt="Image"
                className="custom-image"
              />
            </div>
          </>
        )}
      </div>
    );
}

export default ArtistBox;