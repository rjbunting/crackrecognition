import cv2 as cv
import os
import numpy as np

def getcrack(picture):
    img = cv.imread(picture, cv.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]
    img_crop = img[0:height - 60, 0:width]

    img_smooth = cv.bilateralFilter(img_crop, 5, 25, 25)

    img_proc = cv.threshold(img_smooth, 75, 255, cv.THRESH_BINARY)[1]

    pixels = np.prod(img_proc.shape)
    crackpixels = list(np.unique(img_proc, return_counts=True)[1])[0]
    percentcrack = (crackpixels / pixels) * 100

    cv.imwrite('./output/' + picture.removesuffix('.tif').removeprefix('./input/') + '_proc.tif', img_proc)

    return percentcrack


def main():
    images = os.listdir(f'input/.')
    for image in images:
        percentcrack = getcrack('./input/' + image)
        print(f'{image} = {percentcrack}')

if __name__ == '__main__':
    main()
