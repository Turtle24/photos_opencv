#pylint:disable=no-member
import cv2 as cv
import numpy as np
import random
import os
from textwrap import TextWrapper

# Select random pictures from directory
directory = "Photos"

# Access quotes from txt
quotes = open("quotes.txt", "r")
lines = quotes.readlines()

# Random photo vars
num_files = len([f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))])
rand_pos = random.randint(1,num_files)

# Select a Random photo
def randomPhoto(photo_directory,rand_num):    
    for idx ,filename in enumerate(os.listdir(directory)):
        print(rand_pos)
        if rand_pos == idx:
            print(filename)
            return cv.imread(directory + "/" + filename)


# Select random image effect 
def effectRandomizer(photo):
    rand_pos = random.randint(1,3)
    if rand_pos == 1:
        return cv.cvtColor(photo, cv.COLOR_BGR2GRAY)
    elif rand_pos == 2:
        gray = cv.cvtColor(photo, cv.COLOR_BGR2GRAY)
        gauss = cv.GaussianBlur(gray, (3,3), 0)
        lap = cv.Laplacian(gauss, cv.CV_16S,ksize=3)
        return np.uint8(np.absolute(lap))
    elif rand_pos == 3:
        return photo

# Random text place
rand_pos_text = random.randint(1,len(lines) - 1)
# randomly choose quote and assign it to text variable
def randomQuote(quotelist,ran_num):
    for no, line in enumerate(quotelist,1):
        # insert \n for line split in putText
        tw = TextWrapper()
        tw.width = 50
        # Random quote
        
        if rand_pos == no:            
            if len(line) > 50:
                random_quote = "\n".join(tw.wrap(line))
            else:
                random_quote = line
            return random_quote

# Call random photo
photo = randomPhoto(directory, rand_pos)
# Call random quote
text = randomQuote(lines, rand_pos_text)
# Call random effect and image
img = effectRandomizer(photo)

# Text on image variables
position = (img.shape[1] // 20, img.shape[0] // 2 + img.shape[0] // 5)
font_scale = .6
colour = (255, 255, 255)
thickness = 1
font = cv.FONT_HERSHEY_DUPLEX  
line_type = cv.LINE_AA
text_size, _ = cv.getTextSize(text, font, font_scale, thickness)
line_height = text_size[1] + 5
x, y0 = position

# Place text 
def placeText(text, img):
    if len(text) > 50:

        #Black Outline
        for i, line in enumerate(text.split("\n")):
            y = y0 + i * line_height
            cv.putText(img,
                        line,
                        (x, y),
                        font,
                        font_scale,
                        (0, 0, 0),
                        thickness + 1,
                        line_type)
        # Normal white text
        for i, line in enumerate(text.split("\n")):
            y = y0 + i * line_height
            cv.putText(img,
                        line,
                        (x, y),
                        font,
                        font_scale,
                        colour,
                        thickness,
                        line_type)

    else:

        #Black Outline
        for i, line in enumerate(text.split("\n")):
            y = y0 + i * line_height
            cv.putText(img,
                        line,
                        (x, y),
                        font,
                        font_scale,
                        (0, 0, 0),
                        thickness + 1,
                        line_type)
        # Normal white text
        for i, line in enumerate(text):
            y = y0 + i * line_height
            cv.putText(img,
                        line,
                        (x, y),
                        font,
                        font_scale,
                        colour,
                        thickness,
                        line_type)
                        
    cv.waitKey(0)
    cv.imwrite("image.jpg", img)
# Call place text
placeText(text, img)
