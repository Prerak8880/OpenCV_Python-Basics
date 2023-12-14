import cv2 as cv
import numpy as np

img = cv.imread('Images/1.webp')
 #Gaussian Blur
 output_gaus = cv.GaussianBlur(img, (5,5), 0)

 cv.imshow('Image', output_gaus)
 cv.waitKey(0)
