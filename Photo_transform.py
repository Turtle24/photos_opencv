#pylint:disable=no-member
import cv2 as cv
import numpy as np

img = cv.imread('Photos/PHOTO-2020-12-12-09-49-05.jpg')
# cv.imshow('Kyle', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Kyle', gray)

# Gaussian Blur first
gauss = cv.GaussianBlur(gray, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Laplacian
lap = cv.Laplacian(gauss, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

# canny = cv.Canny(gauss, 150, 175)
# cv.imshow('Canny', canny)

#cv.putText(lap, "If you are distressed by anything external, the pain is not due to the thing itself, but to your estimate of it; and this you have the power to revoke at any moment.― Marcus Aurelius", (0,500), cv.FONT_HERSHEY_TRIPLEX, .5, (255,255,255), 1)
# Insert quote onto image
position = (0, 500)
text = "If you are distressed by anything external, the pain is not due to the thing itself, \nbut to your estimate of it; and this you have the power to revoke at any moment. \nMarcus Aurelius"
font_scale = .5
colour = (255, 255, 255)
thickness = 1
font = cv.FONT_HERSHEY_TRIPLEX
line_type = cv.LINE_AA

text_size, _ = cv.getTextSize(text, font, font_scale, thickness)
line_height = text_size[1] + 5
x, y0 = position
for i, line in enumerate(text.split("\n")):
    y = y0 + i * line_height
    cv.putText(lap,
                line,
                (x, y),
                font,
                font_scale,
                colour,
                thickness,
                line_type)

cv.imshow('Text', lap)

cv.waitKey(0)