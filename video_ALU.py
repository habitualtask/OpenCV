"""산술연산과 논리연산 처리"""
import cv2

original = cv2.imread("song.jpg", cv2.IMREAD_COLOR)
a=91

plus = original+a
minus = original-a
divide = original/a
mult = original*a
AND = cv2.bitwise_and(original,a)
XOR = cv2.bitwise_xor(original,a)

cv2.imshow("original",original)
cv2.imshow("+", plus)
cv2.imshow("-", minus)
cv2.imshow("/", divide)
cv2.imshow("*", mult)
cv2.imshow("AND", AND)
cv2.imshow("XOR",XOR)
cv2.waitKey(0)
cv2.destroyAllWindows()