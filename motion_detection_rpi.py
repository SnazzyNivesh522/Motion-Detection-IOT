import time
import os
import subprocess
import requests
from gpiozero import MotionSensor 

#https://gpiozero.readthedocs.io/en/latest/api_input.html#gpiozero.MotionSensor

PIR_PIN = 4  # PIR sensor is connected to GPIO pin 4
IMAGE_DIR = "captured_images" # Directory to save captured images
SERVER_URL="http://localhost:5000/upload" #flask server api

pir = MotionSensor(PIR_PIN)

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    print(f"Directory {IMAGE_DIR} created.")

def capture_image():
    """
    Captures an image using the libcamera-still command line tool.
    """

    timestamp = time.strftime("%Y%m%d_%H%M%S")  
    file_path = f"{IMAGE_DIR}/image_{timestamp}.jpg"
    
    # Run libcamera-still command to capture the image
    subprocess.run(["libcamera-still", "-o", file_path, "-t", "1"])
    print(f"Captured image saved to: {file_path}")
    
    return file_path

def send_image_to_server(image_path):
    """
    Sends the captured image to the server for further processing.
    """
    with open(image_path, 'rb') as img_file:
        files = {'file': (image_path, img_file, 'image/jpeg')}
        response = requests.post(SERVER_URL, files=files)
        
        if response.status_code == 200:
            print("Image successfully uploaded to server.")
        else:
            print(f"Failed to upload image. Server responded with: {response.status_code}")

def main():
    print("Motion detection started...")
    try:
        while True:
            pir.wait_for_motion()  # Wait for motion to be detected
            print("Motion detected! Capturing image...")

            # Capture image when motion is detected
            image_path = capture_image()

            # Send the image to the server
            send_image_to_server(image_path)

            # Sleep for a short time to prevent multiple captures in quick succession
            time.sleep(5)  

            pir.wait_for_no_motion()  # Wait until motion stops before checking again

    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
    
