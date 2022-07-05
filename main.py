import numpy as np
import matplotlib.pyplot as plt
import imutils 
import cv2  
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

path = '/content/drive/MyDrive/PIM/'
#scale = imread(path+'verticalBars.png')
scale_1 = imread(path+"scaled_1.png")
scale_12 = imread(path+"scaled_1.2.png")
scale_14 = imread(path+"scaled_1.4.png")
scale_16 = imread(path+"scaled_1.6.png")
scale_18 = imread(path+"scaled_1.8.png")
scale_20 = imread(path+"scaled_2.0.png") 
scale_22 = imread(path+"scaled_2.2.png") 


scaled = [scale_1, scale_12, scale_14 ,scale_16 ,scale_18, scale_20, scale_22]

def fourier(img):
  dark_image_grey = rgb2gray(img)
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image_grey))
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  fig, ax = plt.subplots(1,2,figsize=(15,15))
  ax[0].imshow(dark_image_grey, cmap='gray')
  ax[1].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
  
  
 for im in scaled:
  fourier(im)
