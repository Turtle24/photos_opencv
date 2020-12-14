#pylint:disable=no-member
# Necessary imports
import cv2
import numpy as np
#  Importing function cv2_imshow necessary for programming in Google Colab
from google.colab.patches import cv2_imshow

img = cv2.imread("PHOTO-2020-12-12-09-49-05.jpeg")
cv2_imshow(img)

edges = cv2.Canny(img, 100, 200)
cv2_imshow(edges)

cv.waitKey(0)