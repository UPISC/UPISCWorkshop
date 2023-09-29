import cv2               
import numpy as np
import os                                   # Files utilities


im = cv2.imread("Star_sample.jpg")
collor = cv2.imread("background.jpg")

sides = int(np.abs(np.min(im[:,:,0].shape)-np.max(im[:,:,0].shape)*250/350))
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
cv2.imwrite("Star_resized.jpg",img)