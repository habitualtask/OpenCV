"""픽셀단위 공간해상도"""
import cv2

original = cv2.imread("song.jpg", cv2.IMREAD_COLOR)
gray = cv2.imread("song.jpg", cv2.IMREAD_GRAYSCALE)

dst1 = cv2.resize(gray, dsize=(16, 16), interpolation=cv2.INTER_AREA)
dst1 = cv2.resize(dst1, dsize=(413, 531), interpolation=cv2.INTER_AREA)

dst2 = cv2.resize(gray, dsize=(32, 32), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(dst2, dsize=(413, 531), interpolation=cv2.INTER_AREA)

dst3 = cv2.resize(gray, dsize=(64, 64), interpolation=cv2.INTER_AREA)
dst3 = cv2.resize(dst3, dsize=(413, 531), interpolation=cv2.INTER_AREA)

dst4 = cv2.resize(gray, dsize=(128, 128), interpolation=cv2.INTER_AREA)
dst4 = cv2.resize(dst4, dsize=(413, 531), interpolation=cv2.INTER_AREA)

dst5 = cv2.resize(gray, dsize=(256, 256), interpolation=cv2.INTER_AREA)
dst5 = cv2.resize(dst5, dsize=(413, 531), interpolation=cv2.INTER_AREA)

dst6 = cv2.resize(gray, dsize=(512, 512), interpolation=cv2.INTER_AREA)
dst6 = cv2.resize(dst6, dsize=(413, 531), interpolation=cv2.INTER_AREA)

cv2.imshow("Original", original)
cv2.imshow("16*16", dst1)
cv2.imshow("32*32",dst2)
cv2.imshow("64*64", dst3)
cv2.imshow("128*128",dst4)
cv2.imshow("256*256", dst5)
cv2.imshow("512*512",dst6)

cv2.waitKey(0)
cv2.destroyAllWindows()