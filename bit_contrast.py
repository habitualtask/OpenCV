"""BIT단위로 밝기해상도 조절"""
import cv2

original = cv2.imread("song.jpg", cv2.IMREAD_COLOR)
gray = cv2.imread("song.jpg", cv2.IMREAD_GRAYSCALE)
bit1 = gray-1
bit2 = gray-4
bit4 = gray-16
bit8 = gray-255

cv2.imshow("Original", original)
cv2.imshow("1bit", bit1)
cv2.imshow("2bit", bit2)
cv2.imshow("4bit", bit4)
cv2.imshow("8bit", bit8)

cv2.waitKey(0)
cv2.destroyAllWindows()