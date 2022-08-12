from typing import Any, Tuple
import cv2 as cv


# TODO: change this function to contours detection
def crop_image(path: str) -> Any:

    """ Manually crop the image
    to units and tens

    @param path The path to the image
    @return List of croppend images units as first element
        
    """

    image = cv.imread(path)

    # TODO: to be changed
    image_crop = image[90:200, 300:520]

    

    return image_crop

def reshape_image(image, shape: Tuple[int,int,int,int]):

    """Reshape the image matrix 

    @param image The image matrix
    @param shape Tuple containing the return image shape

    @return Image after being reshaped
    """

    img = image.reshape(shape)
    return img

def gray_scale(iamge_mat):

    """Convert the image to a gray scale

    @param image_mat The colored image
    @return image matrix with a gray scale
    """

    gray_img = cv.cvtColor(iamge_mat, cv.COLOR_BGR2GRAY)
    return gray_img

def hist_transform(image_mat, grey=True):

    """Perform a color stabilisation on the image pixels

    @param image_mat Image to be processed
    @param grey True if image_mat is grey scaled image False if not
    @return image matrix with stabilized color
    """

    if not grey:
        r_image, g_image, b_image = cv.split(image_mat)

        r_image_eq = cv.equalizeHist(r_image)
        g_image_eq = cv.equalizeHist(g_image)
        b_image_eq = cv.equalizeHist(b_image)

        image_eq = cv.merge((r_image_eq, g_image_eq, b_image_eq))

    else:
        image_eq = cv.equalizeHist(image_mat)
    
    return image_eq


def threshold_image(image_mat):

    """Apply a binary threshold filter on gray image

    @param image_mat gray scale image
    @return image with the threshold filter
    """

    _, thresholded = cv.threshold(image_mat, 127, 255, cv.THRESH_BINARY)
    return thresholded

def contouring(image_mat):

    """Detecting contours in the image

    @param image_mat gray scale image with threshold filter
    @return ???
    """

    contours, _ = cv.findContours(image=image_mat, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)

    return contours


def tess_processing(image_mat):
    
    """Preprocessing the image for better result

    @param image_mat Image to be processed
    @return Processed image
    """


    processed_image = cv.cvtColor(image_mat, cv.COLOR_BGR2GRAY)
    processed_image = cv.GaussianBlur(processed_image, (3,3), 0)
    processed_image = cv.threshold(processed_image, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    return processed_image






