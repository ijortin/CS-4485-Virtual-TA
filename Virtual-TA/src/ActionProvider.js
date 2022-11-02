import React, { useState, useEffect } from "react";
 let ActionProvider = ({ createChatBotMessage, setState, children }) => {

  const handleHello = () => {
    const botMessage = createChatBotMessage('hi');

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
  let handleDefault = () => {
    const botMessage = createChatBotMessage(
      "Here's what I found for you",
      {
        widget: 'dogPicture',
      }
    );

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
 