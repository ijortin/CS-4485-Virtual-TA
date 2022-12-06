# CS-4485-Virtual-TA
Key Components of this Project:
1. React Frontend
   - Further react-chatbot-kit documentation found here https://fredrikoseberg.github.io/react-chatbot-kit-docs/docs/
   - Action Provider.js
     - This file sends the message from the front end to the backend and handles the call to render the new chat bubble. 
   - Message Parser.js
     - Component that comes with the react-chatbot-kit message. With a python backend, it is used as an intermediary between Action Provider and the message sent. Can be modified to have the messages handled entirely by the frontend.
   - Form.js
      - Visual component that acts as a guide to Latex syntax for the user. 
2. Python Backend
   -  Hosted on Flask. Model built using keras in tensorflow. 
   -  Intents.json
      - Edit this to help train the bot on different questions that can be asked  
