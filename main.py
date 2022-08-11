import cv2 as cv
import numpy as np
from preprocessing import preprocessing
from model import Model
from data import data
from datetime import datetime
from time import strftime





def main():

    model = Model()

    conn = data.connectBd()

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
                timess = datetime.now().time()
                time = timess.strftime("%H:%M:%S")
                data.StreamCiterne(conn, "C1",float(predicted_number),
                                    0.0, 
                                    datetime.now().date(), 
                                    time)
                

            else:
                capt.release()

if __name__ == "__main__":
    main()
