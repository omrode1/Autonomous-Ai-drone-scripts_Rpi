import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

net = None
camera = None

def initialize_detector():
    global net, camera
    net = jetson.inference.detectNet("ssd-mobilenet-v2")
    
    # Replace the following line with appropriate camera initialization for Raspberry Pi
    camera = PiCamera()
    
    print("fakka")

def get_image_size():
    # Replace these lines with appropriate functions for PiCamera
    width, height = camera.resolution
    return width, height

def close_camera():
    # Replace this line with appropriate function for closing PiCamera
    camera.close()

def get_detections():
    person_detections = []
    
    # Capture an image from PiCamera
    raw_capture = PiRGBArray(camera)
    camera.capture(raw_capture, format="bgr")
    img = raw_capture.array
    
    # Perform the detection
    detections = net.Detect(img)
    
    for detection in detections:
        if detection.ClassID == 1:  # remove unwanted classes
            person_detections.append(detection)
    
    # fps calculation (this may need adjustment based on PiCamera usage)
    fps = net.GetNetworkFPS()
    
    return person_detections, fps, img
