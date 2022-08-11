from typing import Any, Tuple
import cv2 as cv


# TODO: change this function to contours detection
def crop_image(path: str) -> Any:

    """ Manually crop the image
    to units and tens

    @param path The path to the image
    @return List of croppend images units as first element
        
    """

    cropped_images = []
    image = cv.imread(path)

    # TODO: to be changed
    units_crop = image[200:201, 200:201]
    tens_crop = image[200:201, 200:201]

    cropped_images.append(units_crop)
    cropped_images.append(tens_crop)

    return cropped_images

def reshape_image(image, shape: Tuple[int,int,int,int]):

    """Reshape the image matrix 

    @param image The image matrix
    @param shape Tuple containing the return image shape

    @return Image after being reshaped
    """

    img = image.reshape(shape)
    return img





