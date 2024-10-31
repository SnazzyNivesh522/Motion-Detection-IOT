import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import ImageUpload from './components/ImageUpload';
import EventList from './components/EventList';
import './App.css';


const App = () => {
  return (
    <div className="container mt-4">
      <h1 className="text-center text-primary">Motion Detection and Identification</h1>
      <ImageUpload />
      <EventList />
    </div>
  );
};

export default App;