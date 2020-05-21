"""1차미분연산자를 이용한 에지 검출과 3가지 마스크"""
import numpy as np
import cv2

def preprocessing(rawimg):
    src = cv2.imread(rawimg)
    processedSrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    return processedSrc

def pad_with(array, pad_width, iaxis, kwargs):
    pad_value = kwargs.get("padder", 0)
    array[:pad_width[0]] = pad_value
    array[-pad_width[1]:] = pad_value
    return array

def padding(array, pad_width):

    paddingarray = np.pad(array, pad_width, pad_with)
    return paddingarray

def convolution(rowlength, columnlength, kernel, array):

    temp = np.zeros((rowlength, columnlength), dtype=np.float_)
    for i in range(rowlength):
        for j in range(columnlength):
            temp[i][j] = np.inner(kernel, array[i:i+3, j:j+3].flatten())
    return temp
if __name__ == "__main__":

    gray_lena = preprocessing("Lenna.png")
    padding_lena = padding(gray_lena, 1)
    rowlength = gray_lena.shape[0]
    columnlength = gray_lena.shape[1]
    roberts_x = np.array([0, 0, -1,
                          0, 1, 0,
                          0, 0, 0])

    roberts_y = np.array([-1, 0, 0,
                          0, 1, 0,
                          0, 0, 0])
    prewitt_x = np.array([-1, -1, -1,
                          0, 0, 0,
                          1, 1, 1])
    prewitt_y = np.array([1, 0, -1,
                          1, 0, -1,
                          1, 0, -1])

    sobel_x = np.array([-1, -2, -1,
                        0, 0, 0,
                        1, 2, 1])
    sobel_y = np.array([1, 0, -1,
                        2, 0, -2,
                        1, 0, -1])

    roberts_x = convolution(rowlength, columnlength, roberts_x, padding_lena)
    roberts_gx = cv2.convertScaleAbs(roberts_x)
    roberts_y = convolution(rowlength, columnlength, roberts_y, padding_lena)
    roberts_gy = cv2.convertScaleAbs(roberts_y)
    roberts_g = cv2.addWeighted(roberts_gx, 1, roberts_gy, 1, 0)
    cv2.imshow("robert", roberts_g)

    prewitt_x = convolution(rowlength, columnlength, prewitt_x, padding_lena)
    prewitt_gx = cv2.convertScaleAbs(prewitt_x)
    prewitt_y = convolution(rowlength, columnlength, prewitt_y, padding_lena)
    prewitt_gy = cv2.convertScaleAbs(prewitt_y)
    prewitt_g = cv2.addWeighted(prewitt_gx, 1, prewitt_gy, 1, 0)
    cv2.imshow("prewitt", prewitt_g)

    sobel_x = convolution(rowlength, columnlength, sobel_x, padding_lena)
    sobel_gx = cv2.convertScaleAbs(sobel_x)
    sobel_y = convolution(rowlength, columnlength, sobel_y, padding_lena)
    sobel_gy = cv2.convertScaleAbs(sobel_y)
    sobel_g = cv2.addWeighted(sobel_gx, 1, sobel_gy, 1, 0)
    cv2.imshow("sobert", sobel_g)
    cv2.waitKey(0)
    cv2.destroyAllWindows()