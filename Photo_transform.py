#pylint:disable=no-member
import cv2 as cv
import numpy as np
import random
import os

# Select random picture
directory = "Photos"

for filename in os.listdir(directory):
    num_files = len([f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))])
    rand_pos = random.randint(1,num_files)
    if num_files == rand_pos:
        photo = cv.imread(directory + "/" + filename)
        #cv.imshow('Kyle', img)

#img = cv.imread(random_filename)
# cv.imshow('Kyle', img)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Kyle', gray)

# Gaussian Blur first
# gauss = cv.GaussianBlur(gray, (3,3), 0)
# #cv.imshow('Gaussian Blur', gauss)

# # Laplacian
# lap = cv.Laplacian(gauss, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

# canny = cv.Canny(gauss, 150, 175)
# cv.imshow('Canny', canny)

# Select random image effect \:D/
def effectRandomizer(photo):
    rand_pos = random.randint(1,10)
    if rand_pos % 2 == 0:
        return cv.cvtColor(photo, cv.COLOR_BGR2GRAY)
    elif rand_pos % 3 == 0:
        gray = cv.cvtColor(photo, cv.COLOR_BGR2GRAY)
        gauss = cv.GaussianBlur(gray, (3,3), 0)
        lap = cv.Laplacian(gauss, cv.CV_64F)
        return np.uint8(np.absolute(lap))

# Access quotes from txt
import random
quotes = open("quotes.txt", "r")
lines = quotes.readlines()
print(lines)
text = ""
# randomly choose quote and assign it to text variable
for no,line in enumerate(lines,1):
    # insert \n for line split in putText
    if len(line) > 50:
        text = line[:50] + "\n" + line[50:]
    # Random quote
    rand_pos = random.randint(1,len(lines))
    if rand_pos == no:
        text = text
#print(text)

# Call random effect and image
img = effectRandomizer(photo)

position = (img.shape[1] // 2 - img.shape[1] // 3, img.shape[0] // 2 + img.shape[0] // 5)
#text = "If you are distressed by anything external, the pain is not due to the thing itself, \nbut to your estimate of it; and this you have the power to revoke at any moment. \nMarcus Aurelius"
font_scale = .6
colour = (255, 255, 255)
thickness = 1
font = cv.FONT_HERSHEY_DUPLEX  
line_type = cv.LINE_AA

text_size, _ = cv.getTextSize(text, font, font_scale, thickness)
line_height = text_size[1] + 5
x, y0 = position
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

cv.imshow('Text', img)

cv.waitKey(0)