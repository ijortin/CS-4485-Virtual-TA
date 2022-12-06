
import React from "react";

  const MessageParser = ({ children, actions }) => {
   //On any message given to chatbot pass it to handle default in action provider to getresponse from backend 
    const parse = (message) => {
      //you could add if or case statements here to let the frontend handle more of the bot responses - need to create accompanying funcs in action provider
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
