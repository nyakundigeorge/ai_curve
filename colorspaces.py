import cv2
import numpy as np


#define function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    #read the current frame from the videocapture object
    _, frame = cap.read()
    #resize the image
    frame = cv2.resize(frame,None, fx=scaling_factor, fy=scaling_factor,interpolation=cv2.INTER_AREA)
    return frame

if __name__ == "__main__":
    #Define the video capture object
    cap = cv2.VideoCapture(0)
    #define the scaling factor for the images
    scaling_factor = 0.5
    #keep reading the frame from the Webcam
    while True:
        #grab the current frame
        frame = get_frame(cap, scaling_factor)
        #convert image to HSV color space
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #define range of skin color in HSV
        lower = np.array([0,70,60])
        upper = np.array([50,150,255])
        #threshold the HSV image to get only skin color
        mask = cv2.inRange(hsv,lower,upper)
        #Bitwise_and between the Mask and Original image
        img_bitwise_and = cv2.bitwise_and(frame,frame,mask=mask)
        #run median blurring
        img_median_blurred = cv2.medianBlur(img_bitwise_and,5)
        #Display the input and output
        cv2.imshow('Input',frame)
        cv2.imshow('Output',img_median_blurred)

        #check if the user hit the 'ESC' key

        c = cv2.waitKey(5)
        if c == 27:
            break

    #close all windows
    cv2.destroyAllWindows()