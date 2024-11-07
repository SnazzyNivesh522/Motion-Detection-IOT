import React, { useState } from 'react';
import api from '../api';

const ImageUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Please select a file to upload.');
      return;
    }
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await api.post('/upload', formData);
      setMessage(`Recognized faces: ${response.data.recognized_faces}`);
    } catch (error) {
      setMessage('Upload failed');
    }
  };
  

  return (
    <div className="mb-4">
      <div className="input-group">
        <input type="file" className="form-control" onChange={handleFileChange} />
        <button className="btn btn-primary" onClick={handleUpload}>Upload</button>
      </div>
      {message && <div className="alert alert-info mt-2">{message}</div>}
    </div>
  );
};

export default ImageUpload;