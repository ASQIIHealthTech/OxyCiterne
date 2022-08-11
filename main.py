import cv2 as cv
import numpy as np
from preprocessing import preprocessing
from model import Model







def main():

    model = Model()

    capt = cv.VideoCapture('assets', 'NumberCounterAnimation.mp4')   

    if capt.isOpened():
        while(capt.isOpened()):

            ret,frame = capt.read()
            if ret:

                units, tens = preprocessing.crop_image(frame)
                units = np.argmax(model.predict(preprocessing.reshape_image(units, (1, 150, 300, 3))))
                tens = np.argmax(model.predict(preprocessing.reshape_image(tens, (1, 150, 300, 3))))

                predicted_number = (tens * 10) + units 

                # TODO: send the predicted number to the database

                

            else:
                capt.release()

if __name__ == "__main__":
    main()
