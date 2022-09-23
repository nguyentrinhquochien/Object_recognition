import numpy as np
import cv2
import keyboard
from numpy import array, arange, uint8 
from matplotlib import pyplot as plt

while True:
    if keyboard.is_pressed('1'):
        img = cv2.imread('input_03.jpg', 0)
        cv2.imshow('Anhinput_03',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('input_03.png', img)
        cv2.destroyAllWindows()
    
    if keyboard.is_pressed('2'):
        img = cv2.imread("input_03.jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Hien", img)
       
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if keyboard.is_pressed('3'):
        img = cv2.imread('input_06.jpg')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if keyboard.is_pressed('4'):
        img = cv2.imread("input_03.jpg")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh_binary = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
        cv2.imshow("Hien", thresh_binary) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    