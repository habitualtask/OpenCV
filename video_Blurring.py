"""영상신호처리 - 블러링"""
import cv2
import numpy as np
image = cv2.imread("Lenna.png")

rows, cols = image.shape[:2]

low_pass_filter_3x3 = np.ones((3, 3), np.float32) / 9.0
low_pass_filter_5x5 = np.ones((5, 5), np.float32) / 25.0
low_pass_filter_7x7 = np.ones((7, 7), np.float32) / 49.0

cv2.imshow('Source', image)

dst = cv2.filter2D(image, -1, low_pass_filter_3x3)
cv2.imshow('low_pass_filter_3x3', dst)

dst = cv2.filter2D(image, -1, low_pass_filter_5x5)
cv2.imshow('low_pass_filter_5x5', dst)

dst = cv2.filter2D(image, -1, low_pass_filter_7x7)
cv2.imshow('low_pass_filter_7x7', dst)

cv2.waitKey()