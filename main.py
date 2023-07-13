from rembg import remove
from PIL import Image


def remove_bg():
    """
    Remove the background of an image using the remove() function and save the output to a file.
    :param image: The input image to remove the background from.
    :type image: PIL.Image.Image
    """
    input_path = "image.png"
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_path = "output.png"
    output_image.save(output_path)

remove_bg()
