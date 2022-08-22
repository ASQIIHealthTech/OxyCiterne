import cv2 as cv
from preprocessing import preprocessing
from data import data
from datetime import datetime
from time import strftime
from pytesseract import image_to_string



def main():


    conn = data.connect_bd()

    capt = cv.VideoCapture(1)   

    while(True):

        ret,frame = capt.read()
        if ret:

            ## preduict the number

            # cropping the image and preprocessed it
            pourcentage_image = preprocessing.crop_image(frame)
            preprocessed_image = preprocessing.tess_processing(pourcentage_image)



            tess_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" --psm 7'
            text = image_to_string(preprocessed_image, lang='letsgodigital', config=tess_dir_config)

            # send the predicted number to the database
            timess = datetime.now().time()
            time = timess.strftime("%H:%M:%S")
            data.stream_citerne(conn, "C1",float(text),
                                0.0, 
                                datetime.now().date(), 
                                time)
                                    
                

        else:
            capt.release()
            print("Something went wrong!!", "Please Contact ASQII", sep="\n")


if __name__ == "__main__":
    main()
