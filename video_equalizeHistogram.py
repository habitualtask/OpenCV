"""히스토그램 평활화, 원본과의 비교코드"""
import cv2

src = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src)
"""원본"""
cv2.imshow("source", src)
"""평활화"""
cv2.imshow("destination", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()