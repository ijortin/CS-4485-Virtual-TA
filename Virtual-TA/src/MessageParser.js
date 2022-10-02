// MessageParser starter code
import React from 'react';
  const MessageParser = ({ children, actions }) => {
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