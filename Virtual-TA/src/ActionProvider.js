import React, { useState, useEffect } from "react";
 const ActionProvider = ({ createChatBotMessage, setState, children }) => {
              // usestate for setting a javascript
    // object for storing and using data
    const [datas, setdatas] = useState({
      message:"",
  });

  const handleDefault = (msg) => {
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title: msg })
      };
      fetch('/data', requestOptions)
          .then(response => response.json())
          .then(data => setdatas({
            message: data.Message,}));

    const botMessage = createChatBotMessage(datas.message);

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };
  
  // Put the handleHello function in the actions object to pass to the MessageParser
  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleDefault,
          },
        });
      })}
    </div>
  );
};
 export default ActionProvider;