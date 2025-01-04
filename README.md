# IoT-Based Surveillance System

![Project Logo](https://via.placeholder.com/150)

Welcome to the **IoT-Based Surveillance System** repository! This project integrates motion detection, image capture, and face recognition to provide a comprehensive surveillance solution using IoT devices. The system is composed of a Raspberry Pi for motion detection, a Flask-based backend server for processing and storing data, and a React frontend for real-time event monitoring and interaction.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Raspberry Pi Setup](#raspberry-pi-setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Motion Detection**: Utilizes a PIR sensor connected to a Raspberry Pi to detect motion.
- **Image Capture**: Automatically captures images when motion is detected.
- **Face Recognition**: Processes captured images to identify known individuals using face recognition.
- **Real-time Monitoring**: Displays detected events and recognized faces on a React-based frontend.
- **Event Tracking**: Stores and retrieves event data using a Flask backend with a SQLAlchemy database.
- **Secure File Handling**: Ensures secure upload and storage of images with proper validations.

## Architecture

The system is divided into three main components:

1. **Raspberry Pi (IoT Device)**: Handles motion detection and image capture. Sends captured images to the backend server for processing.
2. **Backend Server (Flask)**: Receives images, performs face recognition, stores event data, and serves APIs for the frontend.
3. **Frontend Client (React + Vite)**: Provides a user interface to view and interact with detected events and recognized faces.

![Architecture Diagram](https://via.placeholder.com/600x400)

## Directory Structure

```
SnazzyNivesh522-Motion-Detection-IOT/
├── motion_detection_rpi.py
├── client/
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── vite.config.js
│   ├── .gitignore
│   └── src/
│       ├── App.css
│       ├── App.jsx
│       ├── api.jsx
│       ├── main.jsx
│       └── components/
│           ├── EventList.jsx
│           └── ImageUpload.jsx
└── server/
    ├── app.py
    ├── config.py
    ├── extensions.py
    ├── models.py
    ├── requirements.txt
    ├── routes.py
    ├── utils.py
    ├── .gitignore
    └── Training_images/
```

### Overview

- **motion_detection_rpi.py**: Python script running on Raspberry Pi for motion detection and image capture.
- **client/**: React frontend application.
  - **src/components/**: Contains React components for event listing and image uploading.
- **server/**: Flask backend application.
  - **Training_images/**: Directory containing images of known individuals for face recognition.

## Installation

### Prerequisites

- **Raspberry Pi** with GPIO capabilities.
- **Python 3.7+** installed on both the Raspberry Pi and the backend server.
- **Node.js 14+** and **npm** installed for the frontend.
- **Flask**, **SQLAlchemy**, and other Python dependencies.
- **Face Recognition** libraries and dependencies.
- **Git** for version control.

### Backend Setup

1. **Navigate to the Server Directory**:
   ```bash
   cd server
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the `server/` directory with the following variables:
     ```env
     SECRET_KEY=your_secret_key
     SQLALCHEMY_DATABASE_URI=sqlite:///events.db
     UPLOAD_FOLDER=uploads/
     FRONTEND_URL=http://localhost:5173
     ```

5. **Run the Backend Server**:
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000`.

### Frontend Setup

1. **Navigate to the Client Directory**:
   ```bash
   cd client
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Run the Frontend Application**:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

### Raspberry Pi Setup

1. **Ensure All Dependencies Are Installed**:
   - Python packages: `gpiozero`, `requests`, etc.
   - `libcamera-still` tool for image capture.

2. **Configure the `motion_detection_rpi.py` Script**:
   - Ensure the `SERVER_URL` in `motion_detection_rpi.py` points to your backend server's address.

3. **Run the Motion Detection Script**:
   ```bash
   python3 motion_detection_rpi.py
   ```

## Usage

1. **Start All Components**:
   - Ensure the backend server, frontend application, and Raspberry Pi script are all running.

2. **Monitor Events**:
   - Open the frontend at `http://localhost:5173` to view real-time events and recognized faces.

3. **Upload Images Manually**:
   - Use the Image Upload component on the frontend to manually upload images for face recognition.

4. **View Event Details**:
   - The Event List component displays all detected events with timestamps and recognized individuals.

## Technologies Used

- **Frontend**:
  - [React](https://reactjs.org/)
  - [Vite](https://vitejs.dev/)
  - [Bootstrap](https://getbootstrap.com/)
  - [Axios](https://axios-http.com/)

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/)
  - [Flask-CORS](https://flask-cors.readthedocs.io/)
  - [SQLAlchemy](https://www.sqlalchemy.org/)
  - [Face Recognition](https://github.com/ageitgey/face_recognition)
  - [OpenCV](https://opencv.org/)
  - [Pillow](https://python-pillow.org/)

- **IoT**:
  - [Raspberry Pi](https://www.raspberrypi.org/)
  - [GPIO Zero](https://gpiozero.readthedocs.io/)

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**
   ```bash
   git commit -m "Add your message"
   ```

4. **Push to the Branch**
   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Developed with ❤️ by [Nivesh Pritmani](https://github.com/SnazzyNivesh522)*

# Acknowledgments

- Inspired by various IoT and AI surveillance projects.
- Special thanks to the open-source community for providing invaluable tools and libraries.

# Contact

For any inquiries or support, please contact [niveshpritmani@gmail.com](mailto:niveshpritmani@gmail.com).

---
