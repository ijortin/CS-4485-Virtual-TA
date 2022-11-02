
  

  // Config starter code
  import React from 'react'
  import { createChatBotMessage } from "react-chatbot-kit";
  import DogPicture from './DogPicture.js'
  
  const config = {
    initialMessages: [createChatBotMessage(`Welcome to the TA for Data Structures and Algorithms! Ask me a question like what is the space complexity of Selection Sort?`)],
    widgets: [
      {
        widgetName: 'dogPicture',
        widgetFunc: (props) => <DogPicture {...props} />,
      },
    ],
  }
  
  export default config