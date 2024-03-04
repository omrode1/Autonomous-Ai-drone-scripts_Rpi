import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Create a PiCamera object
camera = PiCamera()

# Adjust camera settings as needed
camera.resolution = (640, 480)
camera.framerate = 32

# Create a PiRGBArray object
raw_capture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

# Main capture loop
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    img = frame.array
    
    # Your processing logic here
    
    cv2.imshow("Camera", img)
    key = cv2.waitKey(1) & 0xFF
    
    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break
    
    # Clear the stream for the next frame
    raw_capture.truncate(0)

# Release resources
cv2.destroyAllWindows()
