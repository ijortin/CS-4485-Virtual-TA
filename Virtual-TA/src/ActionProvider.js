import React, { useState, useEffect } from "react";
 const ActionProvider = ({ createChatBotMessage, setState, children }) => {
        // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
      message:"",
  });

  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting a data from api
              setdata({
                  message: data.Message,
              });
          })
      );
  }, []);
  const handleHello = () => {
    const botMessage = createChatBotMessage(data.message);

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };
  const handleGoodbye = () => {
    const botMessage = createChatBotMessage('Goodbye. Talk to you later!');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };
  const handleDefault = () => {
    const botMessage = createChatBotMessage('Hmm. I am not sure how to answer that. Please ask something else');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };
  const handleSelection = () => {
    const botMessage = createChatBotMessage("The space complexity of Selection Sort is O(1)");

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
            handleHello,
            handleGoodbye,
            handleDefault,
            handleSelection,
          },
        });
      })}
    </div>
  );
};
 export default ActionProvider;
 