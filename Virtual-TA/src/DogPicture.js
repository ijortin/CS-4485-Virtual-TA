
import React, { useEffect, useState } from 'react';
import { createChatBotMessage } from "react-chatbot-kit";

const DogPicture = () => {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    fetch('https://dog.ceo/api/breeds/image/random')
      .then((res) => res.json())
      .then((data) => {
        setImageUrl(data.message);
      });
  }, []);

  return (
    <div> {imageUrl} </div>
  );
};

export default DogPicture;