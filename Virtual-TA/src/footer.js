import React from "react";

const Footer = () => (
  <div className="footer">
    //Elements of footer - each contain an associated UTD link to follow the style of the other UTD pages
    <a
          className="App-link"
          href="https://www.utdallas.edu/"
          target="_blank"
          rel="noopener noreferrer"
        >
          UTDallas Homepage
        </a>

        <a
          className="App-link"
          href="https://elearning.utdallas.edu/ultra/institution-page"
          target="_blank"
          rel="noopener noreferrer"
        >
          UTDallas Elearning
        </a>
        <a
          className="App-link"
          href="https://coursebook.utdallas.edu/"
          target="_blank"
          rel="noopener noreferrer"
        >
          UTDallas Coursebook
        </a>
  </div>
);

export default Footer;
