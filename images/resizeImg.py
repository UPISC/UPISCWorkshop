'''

cd "/mnt/d/UPISCWorkshop/images"

'''

import cv2               
import numpy as np
import os                                   # Files utilities


im_in = "Bedewy.jpg"
ratio = 300/350

im_out = im_in[:-4]+"_resized.jpg"
collor = cv2.imread("background.jpg")
direction = "height"
im = cv2.imread(im_in)

if direction == "width":
    sides = int(len(im[:,0,0])*ratio - len(im[0,:,0]))
    blank = im.copy()
    if sides % 2 > 0:
        blank = blank[:,:int(sides/2)+1,:]
    blank[:,:,0] = collor[0,0,0]
    blank[:,:,1] = collor[0,0,1]
    blank[:,:,2] = collor[0,0,2]
    blank2 = blank.copy()
    if sides % 2 > 0:
        blank2 = blank2[:,:-1,:]
    
    img = np.append(blank2,im,axis=1)
    img = np.append(img,blank,axis=1)

else:
    sides = int(len(im[0,:,0])/ratio - len(im[:,0,0]))
    blank = im.copy()
    if sides % 2 > 0:
        blank = blank[:int(sides/2)+1,:,:]
    blank[:,:,0] = collor[0,0,0]
    blank[:,:,1] = collor[0,0,1]
    blank[:,:,2] = collor[0,0,2]
    blank2 = blank.copy()
    if sides % 2 > 0:
        blank2 = blank2[:-1,:,:]
    
    img = np.append(blank2,im,axis=0)
    img = np.append(img,blank,axis=0)
    
cv2.imwrite(im_out,img)