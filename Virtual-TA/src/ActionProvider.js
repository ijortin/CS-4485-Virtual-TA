import React, { useState, useEffect } from "react";
 const ActionProvider = ({ createChatBotMessage, setState, children }) => {
              // usestate for setting a javascript
    // object for storing and using data
    const [datas, setdatas] = useState({
      message:"",
  });

  const handleDefault = async (msg) => {
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title: msg })
      };
      const response = await (await fetch('/data', requestOptions)).json()
           setdatas({
            message: response.Message,})
            console.log(response)


    const botMessage = createChatBotMessage(response.Message);

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