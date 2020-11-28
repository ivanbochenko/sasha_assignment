import os

HEADER = 3
OPTION_RANGE = 4
RED = 0
GREEN = 1
BLUE = 2

def create_blank_image(rows, cols):
    """Create image cols wide and with height rows. Pixels contain [0,0,0].

    Args:
        rows (int): number of rows in new image
        cols (int): number of columns for new image

    Returns:
        list : 2D list containing blank image
    """

    # Can also create the blank image like this:
    #   new_image = [[[0] * 3] * cols] * rows

    new_image = []

    for row in range(rows):
        new_image.append([])    # create a new row
        for col in range(cols):
            new_image[row].append([0, 0, 0]) # append a new pixel to the row

    return new_image

def negative(image_list):
    """Create a negative of the image

    Args:
        image_list (list): 2D list containging an image

    Returns:
        list: 2D list containing a negative image
    """

    num_rows = len(image_list)      # Find the number of rows in the image
    num_cols = len(image_list[0])   # Find the number of cols in the image

    new_image = create_blank_image(num_rows, num_cols)

    for row in range(num_rows):
        for col in range(num_cols):
            current_pixel = image_list[row][col]
            new_pixel = new_image[row][col]
            new_pixel[RED] = 255 - current_pixel[RED]
            new_pixel[GREEN] = 255 - current_pixel[GREEN]
            new_pixel[BLUE] = 255 - current_pixel[BLUE]
    return new_image


def crop(image_list, crop_X, crop_Y, crop_width, crop_height):
    """Crop image with origin crop_X, crop_Y and given width and height.

    Args:
        image_list (list): the image
        crop_X (int): X coordinate, counting from 0, of the 
                      top-left pixel of the cropped region.
        crop_Y (int): Y coordinate, counting from 0, of the 
                      top-left pixel of the cropped region.
        crop_width (int): width of cropped region in pixels.
        crop_height (int): height of cropped region in pixels.

    Returns:
        list : 2D list containing cropped image
    """
    new_image = create_blank_image(crop_width, crop_height)


    for row in range(crop_width):
        for col in range(crop_height):
            current_pixel = image_list[row + crop_Y][col + crop_X]
            new_pixel = new_image[row][col]
            new_pixel[RED] = current_pixel[RED]
            new_pixel[GREEN] = current_pixel[GREEN]
            new_pixel[BLUE] = current_pixel[BLUE]
    return new_image
    


def rotate_left_90(image_list):
    """Rotate an image 90 degrees left

    Args:
        image_list (list): image to rotate.

    Returns:
        list : rotated image
    """

    rotated90_image = list(zip(*image_list[::-1]))
    rotated180_image = list(zip(*rotated90_image[::-1]))
    rotated270_image = list(zip(*rotated180_image[::-1]))

    return rotated270_image


def blur(image_list):
    """Blur an image

    Args:
        image_list (list): 2D list containing the image pixels.

    Returns:
        list: 2D list containing the blurred image pixels.
    """
    num_rows = len(image_list)      # Find the number of rows in the image
    num_cols = len(image_list[0])   # Find the number of cols in the image

    new_image = create_blank_image(num_rows, num_cols)

    for row in range(num_rows):
        for col in range(num_cols):
            current_pixel = image_list[row][col]
            new_pixel = new_image[row][col]
            new_pixel[RED] = current_pixel[RED]
            new_pixel[GREEN] = current_pixel[GREEN]
            new_pixel[BLUE] = current_pixel[BLUE]
    return new_image



def get_valid_filename(prompt):
    """Use prompt (a string) to ask the user to type the name of a file. If
	the file does not exist, keep asking until they give a valid filename.

        Args:
        prompt (str): prompt for the user

    Returns:
        str : name of the file
    """
    filename = input(prompt)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(prompt)
    return filename


def print_menu():
    """Print the menu for the application
    """
    print("\n\n\toptions: ")
    print("\t\t[1]  negative")
    print("\t\t[2]  rotate left 90")
    print("\t\t[3]  crop")
    print("\t\t[4]  blur")


def get_menu_option(prompt):
    """Get the menu option from the user and return the option.

    Args:
        prompt (str): text for prompt

    Raises:
        ValueError: Use exception to trap cases where the user has not entered
                    a valid number

    Returns:
        int : option number
    """
    valid_option = False

    while not valid_option:
        print_menu()
        try:
            option = int(input(prompt))
            if option in range(1, OPTION_RANGE + 1):
                valid_option = True
            else:
                raise ValueError
        except ValueError:
            print("\n\n\tthat's not a valid choice, please try again.")
    return option


def read_image(filename):
    """Read a PPM image from filename

    Args:
        filename (str): name of file

    Returns:
        list: 2D list containing the image
    """
    file = open(filename, 'r')

    # Ignore the first line, we don't need it
    file.readline()
    dimensions = file.readline().split()
    columns, rows = int(dimensions[0]), int(dimensions[1])

    # Ignore the third line, assume colour depth is 255
    file.readline()

    # Read the remaining lines into a list
    file_contents = file.readlines()

    # merge the lines of the list into a single 1D list
    # convert the strings to integers.
    all_numbers = []
    for line in file_contents:
        all_numbers += [int(j) for j in line.rstrip().split()]
   
    # Transform the file contents into a 2D list with the dimensions of the image

    image = []
    offset = 0

    for row in range(rows):
        image.append([])
        for col in range(columns):
            rgb = all_numbers[offset : offset + 3]
            image[row].append(rgb)
            offset += 3
    
    return image


def write_image(image, filename):
    """Write a 2D list representing the image to the filename

    Args:
        image (list): 2D list containing image
        filename (str): name of file to write
    """

    rows = len(image)
    cols = len(image[0])

    file = open(filename, 'w')
    file.write("P3\n{0:d} {1:d}\n255\n".format(cols, rows))

    for row in range(rows):
        for col in range(cols):
            rgb = image[row][col]
            file.write("{} {} {}  ".format(rgb[RED], rgb[GREEN], rgb[BLUE]))
        file.write("\n")


def get_dimensions():
    """Get the dimensions of the crop region

    Returns:
        tuple: contains the X,Y origin of the cropped region and the width
                and height of the crop region.
    """
    dimensions_string = input(
        "\t\tEnter the origin x,y and the width and height separated by commas: ")\
            .split(',')
    return int(dimensions_string[0]), int(dimensions_string[1]),\
             int(dimensions_string[2]), int(dimensions_string[3])


def main():
    print("Welcome to the Portable Pixmap (PPM) Image Editor!")

    prompt = "\n\tenter the name of the image file: "
    filename = get_valid_filename(prompt)

    image_list = read_image(filename)

    output_image_filename = input("\n\tenter the name of the output file: ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        new_image = negative(image_list)
    elif menu_choice == 2:
        new_image = rotate_left_90(image_list)
    elif menu_choice == 3:
        crop_X, crop_Y, width, height = get_dimensions()
        new_image = crop(image_list, crop_X, crop_Y, width, height)
    elif menu_choice == 4:
        new_image = blur(image_list)
    
    write_image(new_image, output_image_filename)
    
    print("\nImage written to file", output_image_filename)


if __name__ == '__main__':
    main()