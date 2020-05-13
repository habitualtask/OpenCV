import cv2
import numpy as np

image = cv2.imread("Lenna.png")

sharpening_1 = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
sharpening_2 = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
sharpening_3 = np.array([[1, -2, 1],[-2, 5, -2],[1, -2, 1]])

dst = cv2.filter2D(image, -1, sharpening_1)
cv2.imshow('Sharpening1', dst)

dst = cv2.filter2D(image, -1, sharpening_2)
cv2.imshow('Sharpening2', dst)

dst = cv2.filter2D(image, -1, sharpening_3)
cv2.imshow('Sharpening3', dst)
cv2.waitKey()