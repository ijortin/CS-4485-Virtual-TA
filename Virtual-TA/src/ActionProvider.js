import React from 'react';
 const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMessage = createChatBotMessage('Hello. Nice to meet you.');

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
 