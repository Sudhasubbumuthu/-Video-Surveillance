#Video-Surveillance
Tech stacks and functionalities used:

Python: The project is written in Python, a versatile programming language often used for various applications, including computer vision and automation tasks.

OpenCV (cv2): OpenCV (Open Source Computer Vision Library) is a popular library for computer vision tasks. It's used here for capturing video frames from the webcam, performing image processing tasks like converting to grayscale, applying Gaussian blur, and finding the absolute difference between frames to detect motion.

imutils: This library provides convenience functions to make basic image processing operations simpler with OpenCV. It's used here for resizing frames.

Twilio API: Twilio is a cloud communications platform for building SMS, Voice, and Messaging applications. In this project, the Twilio API is used for sending SMS alerts when motion is detected.

Threading: Threading is utilized to play the alarm sound concurrently with the main program execution. This allows the program to continue running while the alarm is sounding.

Winsound: This module provides access to the basic sound playing machinery provided by Windows. It's used here to generate an alarm sound when motion is detected.

Global Variables: Global variables are used to control the state of the alarm, alarm mode, alarm counter, and last alert time.

Functionality:

The webcam captures frames continuously.
If the alarm mode is activated (t key pressed), the system monitors for motion.
Motion detection is performed by calculating the absolute difference between the current frame and the initial frame captured when the program starts.
If motion is detected, a threshold sum is computed, and if it exceeds a certain value, an SMS alert is sent using the Twilio API.
An alarm sound is played if motion is detected for a certain duration.
This project could serve as a simple surveillance system for monitoring motion in a specific area using a webcam and receiving alerts via SMS.
