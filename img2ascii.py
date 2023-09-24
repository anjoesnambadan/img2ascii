from PIL import Image
import numpy as np
import math
import cv2
from colorama import Fore, Style

def get_image_from_webcam():
    cap = cv2.VideoCapture(0)

    if(cap.isOpened() == False):
        print("Error opening video stream or file")
    else:
        ret, frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()
        return frame
    return None

def resize_image_for_PIL(img, new_width):
    (width, height) = img.size
    new_height = math.floor((height/width)*new_width)
    return img.resize((new_width, new_height))

def resize_image_for_numpy(img, new_width):
    (height, width) = img.shape[:2]
    new_height = math.floor((height/width)*new_width)
    return cv2.resize(img, (new_width, new_height))

def construct_pixel_matrix(img):
    return np.array(img)

def img_to_grayscale_luminanace(pixel_matrix):
    return np.dot(pixel_matrix[...,:3], [0.21, 0.72, 0.07])

def img_to_grayscale_average(pixel_matrix):
    return np.mean(pixel_matrix[...,:3], axis=-1)

def img_to_grayscale_lightness(pixel_matrix):
    rgb_values = pixel_matrix[...,:3]
    max_rgb = np.max(rgb_values, axis=-1)
    min_rgb = np.min(rgb_values, axis=-1)
    return (max_rgb + min_rgb)/2

def create_flag_overlay(pixel_matrix):
    flag_overlay = np.sum(((pixel_matrix//128) * [4, 2, 1]), axis=-1)
    return flag_overlay

def get_map():
    map = tuple("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    return map

def img_to_ascii(gray_matrix):
    map = get_map()
    val = np.floor((gray_matrix / 256) * 65).astype(int)
    return np.vectorize(lambda val: map[val])(val)

def print_result(ascii_matrix, flag):
    height, width = ascii_matrix.shape
    for x in range(height):
        for y in range(width):
            if(flag[x][y] == 0):
                print(Fore.BLACK + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 1):
                print(Fore.BLUE + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 2):
                print(Fore.GREEN + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 3):
                print(Fore.CYAN + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 4):
                print(Fore.RED + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 5):
                print(Fore.MAGENTA + ascii_matrix[x][y]*3, end='')
            elif(flag[x][y] == 6):
                print(Fore.YELLOW + ascii_matrix[x][y]*3, end='')
            else:
                print(Fore.WHITE + ascii_matrix[x][y]*3, end='')
        print()
    print(Style.RESET_ALL)

def ascii_from_path(path):
    img = Image.open(path)
    img = resize_image_for_PIL(img, 300)
    pixel_matrix = construct_pixel_matrix(img)
    flag = create_flag_overlay(pixel_matrix)
    gray_matrix = img_to_grayscale_average(pixel_matrix)
    ascii_matrix = img_to_ascii(gray_matrix)
    print_result(ascii_matrix, flag)

def ascii_from_webcam():
    img = get_image_from_webcam()
    pixel_matrix = resize_image_for_numpy(img, 350)
    flag = create_flag_overlay(pixel_matrix)
    gray_matrix = img_to_grayscale_average(pixel_matrix)
    ascii_matrix = img_to_ascii(gray_matrix)
    print_result(ascii_matrix, flag)

def main():
    choice = input("Welcome to ASCII Art Generator!\n(1) Webcam\n(2) Image\nEnter choice: ")
    if(choice == '1'):
        img = ascii_from_webcam()
    elif(choice == '2'):
        path = input("Enter path to image: ")
        img = ascii_from_path(path)
    else:
        print("Invalid choice")
        return
    
main()