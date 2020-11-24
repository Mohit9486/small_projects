#impoting Libraries
import numpy as np                 
import matplotlib.pyplot as plt    
import cv2                          
import easygui
import tkinter as tk
from tkinter import filedialog
import sys
import os
from PIL import Image,ImageTk
from tkinter import *
import imageio


#fileopenbox opens the box to choose file and help us store file path as string 
def upload():
    path = easygui.fileopenbox()
    cartoonify(path)


def cartoonify()
    #read the image
    im = cv2.imread(path)
    im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    if im is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    im1 = cv2.resize(im,(960,540))
    
    #Now I will transform image to grayscale
    grayim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im2 = cv2.resize(im,(960,540))

    #Smoothening the grayscale image
    smoothim = cv2.medianBlur(grayim,5)
    im3 = cv2.resize(im,(960,540))

    #Retrieving the edges of an image 
    edge = cv2.adaptiveThreshold(smoothim,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    im4 = cv2.resized(im,(960,540))

    colorim = cv2.bilateralFilter(im,9,300,300)
    im5 = cv2.resize(colorim,(960,540))

    cartoon = cv2.bitwise_and(colorim,colorim,mask=edge)
    im6 = cv2.resize(cartoon,(960,540))

    images = [im1,im2,im3,im4,im5,im6]
    fig,axes = plt.subplot(3,2,figsize = (8,8),subplot_kw = {'xticks': [],'yticks'=[]},gridspec_kw=dict(hspace=0.1,wspace=0.1))

    for i,ax in enumerate(axes.flat):
        ax.imshow(images[i],cmap='gray')
    
    plt.show()

def save(im6,path):
    name = filedialog.asksaveasfilename(filetypes=[('JPG','*.jpg')],
    initialdir = os.getcwd(),title = 'Save file')
    cv2.cvtColor(im6,cv2.COLOR_RGB2BGR).save(f'{name}.jpg',save_all=True)
    

