import React, { useState} from "react";
 const ActionProvider = ({ createChatBotMessage, setState, children }) => {
              // usestate for setting a javascript
    // object for storing and using data
    const [datas, setdatas] = useState({
      message:"",
  });
//API call to send msg to backend and receive response to compose new message
  const handleDefault = async (msg) => {
   //Headers and options for request
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title: msg })
      };
   //wait for data sent from backend
      const response = await (await fetch('/data', requestOptions)).json()
           setdatas({
            message: response.Message,})
            console.log(response)

//render botMessage using botResponse
    const botMessage = createChatBotMessage(response.Message);
//maintain history for render all past messages
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };
  
  // Pass the handle default message function to messageparser
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
