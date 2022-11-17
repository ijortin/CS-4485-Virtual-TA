<<<<<<< Updated upstream
// MessageParser starter code
import React, { useState, useEffect } from "react";

  const MessageParser = ({ children, actions }) => {
  
    const parse = (message) => {
        actions.handleDefault(message);
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
=======
// MessageParser starter code
import React from "react";

  const MessageParser = ({ children, actions }) => {

    const parse = (message) => {
        actions.handleDefault(message);
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
>>>>>>> Stashed changes
  export default MessageParser;