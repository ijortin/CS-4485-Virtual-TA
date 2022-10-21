import React from "react"
import logo from './robotta.PNG';
import './App.css';
import Footer from './footer'
import Chatbot from "react-chatbot-kit";
import './main.css';
import config from "./config";
import MessageParser from "./MessageParser";
import ActionProvider from "./ActionProvider";
import { MathJax, MathJaxContext } from "better-react-mathjax";
import Form from "./Form.js"
const equation = "`k_{n+1} = n^2 + k_n^2 - k_{n-1}`";
const blockFormula = `\\int_0^\\infty x^2 dx`; 
const conf = {
  loader: { load: ["input/asciimath"] },
  asciimath: {
    displaystyle: true,
    delimiters: [
      ["$", "$"],
      ["`", "`"]
    ]
  }
};
function App() {
  return (

    <div className="App">
      <div className="form">
              <Form></Form>
              </div>
              help
        <div className = "img"><img src={logo} className="App-logo" alt="logo" /></div>
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
