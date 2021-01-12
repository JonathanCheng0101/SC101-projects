"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:stancodoshop
name:Jonathan Cheng
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
         #想成一顆一顆的pixel，所以不要去用甚麼img.width

    dist = ((pixel.red - red)**2 + (pixel.green-green)**2 +(pixel.blue- blue)**2)**(1/2)

    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixel_red = 0
    pixel_green = 0
    pixel_blue = 0
    for pixel in pixels:
        pixel_red += pixel.red
        pixel_green += pixel.green
        pixel_blue += pixel.blue

    red = pixel_red/len(pixels)
    green = pixel_green/len(pixels)
    blue = pixel_blue/len(pixels)

    rgb =[red,green,blue]
    return rgb



def get_best_pixel(pixels):
    #針對每一個(x,y)上的候選象素，找出最棒的pixel
    #input 一個list, output出一個pixel
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best = pixels[0]
    rgb = get_average(pixels)
    best_dist = get_pixel_dist(pixels[0], rgb[0],rgb[1],rgb[2])


    for pixel in pixels:
        dist = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])
        if dist < best_dist:
            best = pixel


    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect


    for x in range(width):     #因為是要從一個區間(ex 0~ 300做迴圈，如果單用一個image.width就只會跑一次not good good)
        for y in range(height):
            pixels = []

            for image in images:
                pixel = image.get_pixel(x,y)
                pixels.append(pixel)    #建造出在點(x,y)上所有的pixel,並把它存在list pixels裡面


            best = get_best_pixel(pixels)         #得到每個(x,y)的最佳點，並且把rgb都附值
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue





    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):  #把檔案後面有jpg的玩意都弄下來
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]   #把terminal上面的東東叫出來，所以[1]的話就會是你輸入的檔名像是clocl tower
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
