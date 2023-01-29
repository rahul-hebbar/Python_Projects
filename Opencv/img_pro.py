import numpy as np
import cv2.cv2 as cv2
import matplotlib.pyplot as plt
import math

class Grey_Img():
    def __init__(self,image):
        assert len(image.shape) == 2, f'Image input shape {image.shape}: need grayscale image'
        self.image = image

    def histogram(self,plot=True):
        legend = np.arange(256)
        image = np.sort(np.ravel(self.image))
        np_grey = np.pad(np.bincount(image),(0,255-image[-1]),'constant')
        if plot == True:
            plt.bar(legend,np_grey)
            plt.show()
        if plot == False:
            return np_grey

    def brightness(self,value):
        assert type(value) == int, f'given value {value}: has to be integer type'
        self.image = np.add(self.image,np.full(self.image.shape, value, dtype=int))
        self.image = np.clip(self.image,0,255)
        plt.imshow(self.image, cmap='gray', vmin=0, vmax=255)
        plt.show()
        self.histogram()

    def contrast(self,value):
        assert value > 0, f'given value {value}: cannot be less than or equal to 0'
        self.image = self.image*value
        self.image = np.where(self.image<=255,np.ceil(self.image).astype(np.int32),255)
        plt.imshow(self.image, cmap='gray', vmin=0, vmax=255)
        plt.show()
        self.histogram()

    def invert(self):
        self.image = 255 - self.image
        plt.imshow(self.image,cmap='gray',vmin=0, vmax=255)
        plt.show()
        self.histogram()

    def auto_contrast_adjust(self):
        a_high,a_low = np.max(self.image),np.min(self.image)
        self.image = np.subtract(self.image,np.full(self.image.shape,a_low,dtype=int)) 
        self.image = np.ceil(self.image*(255/(a_high-a_low))).astype(int)
        self.image = np.clip(self.image,0,255)
        plt.imshow(self.image,cmap='gray',vmin=0,vmax=255)
        plt.show()
        self.histogram()

    def mod_auto_contrast_adjust(self):
        p = 0.005
        histo = self.histogram(plot=False)
        shape = self.image.shape
        for i in range(histo.shape[0]):
            if histo[i] >= shape[0]*shape[1]*p:
                a_low = i
                break
        for i in range(histo.shape[0]-1,-1,-1):
            if histo[i] >= shape[0]*shape[1]*(p):
                a_high = i
                break
        for i in range(shape[0]):
            for j in range(shape[1]):
                if self.image[i][j] < a_low:
                    self.image[i][j] = 0
                elif self.image[i][j] > a_high:
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = np.ceil((self.image[i][j]-a_low)*255/(a_high-a_low))
        plt.imshow(self.image,cmap='gray',vmin=0,vmax=255)
        plt.show()
        self.histogram()

if __name__ == "__main__":

    img = cv2.imread("dog.jpg",0)
    # plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    # plt.show()
    grey = Grey_Img(img)
    grey.mod_auto_contrast_adjust()

    # arr = np.array([[1,2,3,4],[5,6,7,8]])
    # arr += 2
    # print(arr)