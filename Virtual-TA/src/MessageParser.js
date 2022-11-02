// MessageParser starter code
import React, { useState, useEffect } from "react";

  const MessageParser = ({ children, actions }) => {
    var jsonData = {
      "users": [
          {
              "name": "alan", 
              "age": 23,
              "username": "aturing"
          }]
        }
    const parse = (message) => {
      if (message.includes('hello')) {
        actions.handleHello();
      }
      else if (message.includes('bye')) {
        actions.handleGoodbye();
      }
      else if (message.includes('space')) {
        actions.handleSelection();
      }
      else{
        fetch('http://127.0.0.1:5000/predict', {  // Enter your IP address here

        method: 'POST', 
        mode: 'cors', 
        body: JSON.stringify(jsonData) // body data type must match "Content-Type" header
  
      }).then((response) => response.json())
      .then((data) => {
         console.log(data);
         // Handle data
      })
      .catch((err) => {
         console.log(err.message);
      });
        
        actions.handleDefault();}
    };
  
    return (
      <div>
        {React.Children.map(children, (child) => {
          return React.cloneElement(child, {
            parse: parse,
            actions: {},
          });
        })}
      </div>
    );
  };
  export default MessageParser;