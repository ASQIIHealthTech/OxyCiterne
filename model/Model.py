import os
import numpy as np
from tensorflow import keras
from preprocessing import preprocessing



WEIGHT_PATH = os.path.join('weights', 'model.h5')

class Model():
    """The model implemented in a class\n

    Methods:\n
        predict Predict the digit in the image\n
        @param image Image to be predicted\n
        @return Digit predicted
    """

    def __init__(self) -> None:

        self.model =  keras.models.load_model(WEIGHT_PATH)

    def predict(self, image) -> int:

        shape = (1, 150, 300, 3)
        probas = self.model.predict(preprocessing.reshape_image(image, shape))  
        return np.argmax(probas)
    


    