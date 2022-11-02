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
  export default MessageParser;