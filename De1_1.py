import cv2
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import resize
import matplotlib.pyplot as plt

img = cv2.imread('input_05.png')

gray = cv2.imread('input_05.png', 0)  
color = cv2.imread('input_05.png', 1)
normal = cv2.imread('input_05.png', -1)
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
ret, thresh5 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
thresh6 = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh7 = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

plt.subplot(251)
plt.imshow(gray)

plt.subplot(252)
plt.imshow(color)

plt.subplot(253)
plt.imshow(normal)

plt.subplot(254)
plt.imshow(thresh1)

plt.subplot(255)
plt.imshow(thresh2)

plt.subplot(256)
plt.imshow(thresh3)

plt.subplot(257)
plt.imshow(thresh4)

plt.subplot(258)
plt.imshow(thresh5)

plt.subplot(259)
plt.imshow(thresh6)

plt.subplot(2, 5 ,10)
plt.imshow(thresh7)

plt.show()
plt.waikey(0)