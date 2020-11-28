RED = 0
GREEN = 1
BLUE = 2


def copy(image_list):

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


def main():

    one_pixel = [[[0, 255, 175]]]

    tinypix = [[[0, 0, 0], [100, 0, 0], [0, 0, 0], [255, 0, 255]],\
                [[0, 0, 0], [0, 255, 175], [0, 0, 0], [0, 0, 0]],\
                [[0, 0, 0], [0, 0, 0], [0, 15, 175], [0, 0, 0]],\
                [[255, 0, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255]]]

    eightx4_pixels = [[[255, 255, 0], [100, 0, 0], [0, 0, 0], [255, 0, 255]],\
                        [[0, 0, 0], [0, 255, 175], [0, 0, 0], [0, 102, 255]],\
                        [[0, 102, 255], [0, 0, 0], [0, 15, 175], [0, 0, 0]],\
                        [[255, 0, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255]],\
                        [[0, 0, 0], [100, 0, 0], [255, 255, 0], [255, 0, 255]],\
                        [[51, 204, 51], [0, 255, 175], [0, 0, 0], [0, 0, 0]],\
                        [[0, 0, 0], [0, 0, 0], [0, 15, 175], [0, 102, 255]],\
                        [[255, 0, 255], [51, 204, 51], [0, 0, 0], [255, 255, 255]]]

    new_image = copy(tinypix)
    if new_image == tinypix:
        print("The same!")


if __name__ == '__main__':
    main()