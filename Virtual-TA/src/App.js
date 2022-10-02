import logo from './robotta.PNG';
import './App.css';
import Footer from './footer'
import Chatbot from "react-chatbot-kit";
import './main.css';
import config from "./config";
import MessageParser from "./MessageParser";
import ActionProvider from "./ActionProvider";

function App() {
  return (

    <div className="App">
        <div className = "img"><img src={logo} className="App-logo" alt="logo" /></div>
      <div className = "intro">
        <p  >
          Welcome to your Virtual TA!
        </p>
        </div>
        <div className = "info">
        <p>
          Data Structures and Algorithmic Analysis
        </p>
        <p>
          To begin click on the chat bubble in the bottom right
        </p>
         </div>
        <div className = "Bot">
        <Chatbot
        config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}
      />
      </div>
      <Footer/>
    </div>
   
  );
}

export default App;
