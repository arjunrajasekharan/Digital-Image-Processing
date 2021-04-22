import numpy as np
import cv2
import math
import os


image = cv2.imread("pisa.jpeg")
angle=4
r_angle=angle

angle=math.radians(angle)
cosine=math.cos(angle)
sine=math.sin(angle)
height=image.shape[0]
width=image.shape[1]


new_height  = round(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine))+1
new_width  = round(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine))+1


output=np.zeros((new_height,new_width,image.shape[2]))


original_centre_height   = round(((image.shape[0]+1)/2)-1)
original_centre_width    = round(((image.shape[1]+1)/2)-1)


new_centre_height= round(((new_height+1)/2)-1)
new_centre_width= round(((new_width+1)/2)-1)

for i in range(height):
    for j in range(width):

        y=image.shape[0]-1-i-original_centre_height
        x=image.shape[1]-1-j-original_centre_width

        new_y=round(-x*sine+y*cosine)
        new_x=round(x*cosine+y*sine)

        '''since image will be rotated the centre will change too,
           so to adust to that we will need to change new_x and new_y with respect to the new centre'''
        new_y=new_centre_height-new_y
        new_x=new_centre_width-new_x

 
        if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
            output[new_y,new_x,:]=image[i,j,:]

cv2.imwrite("inter.jpg",output)

img=output
height,width,c=img.shape

for i in range(width):
    for j in range(height):
        if img[j,i,0]==0 and img[j,i,1]==0 and img[j,i,2]==0:
            if j<height -1 and i<width -1 and j>1 and i>1:

                img[j,i,0]=(img[j+1,i,0]+img[j-1,i,0]+img[j,i+1,0]+img[j,i-1,0])/4
                img[j,i,1]=(img[j+1,i,1]+img[j-1,i,1]+img[j,i+1,1]+img[j,i-1,1])/4
                img[j,i,2]=(img[j+1,i,2]+img[j-1,i,2]+img[j,i+1,2]+img[j,i-1,2])/4
cv2.imwrite("Rotated_Pisa.png",img)
os.remove("inter.jpg")

