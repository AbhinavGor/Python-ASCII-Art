from PIL import Image

ASCII_CHARS = [chr(i) for i in range(33,126)]

def scale_image(image, new_width = 300):
    """Resizes image preserving aspect ratio"""
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio*new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_image_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=60):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int((pixel_value/range_width)*6)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=300):
    image = scale_image(image)
    image = convert_image_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try: 
        image = Image.open(image_filepath)
    except:
        print("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        
        return
    
    image_ascii = convert_image_to_ascii(image)
    with open("Output.txt", "w") as text_file:
        print(image_ascii, file=text_file)
    # print(image_ascii)

if __name__ == '__main__':
    import sys
    image_filepath = 'C:\\Users\\Abhinav\\OneDrive\\Desktop\\Python\\Python-ASCII-Art\\images\\nat1.jpg'
    handle_image_conversion(image_filepath)