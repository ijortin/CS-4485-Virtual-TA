
import './App.css';
import Footer from './footer'
import Chatbot from "react-chatbot-kit";
import './main.css';
import config from "./config";
import MessageParser from "./MessageParser";
import ActionProvider from "./ActionProvider";
import Form from "./Form.js"
import React, { useState, useEffect } from "react";
import "./App.css";
  


  

function App() {

  return(
    
    <div className="App">
      <div className="form">
              <Form></Form>
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
