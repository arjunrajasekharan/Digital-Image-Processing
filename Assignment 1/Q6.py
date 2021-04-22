import cv2
def histEq(img,rows,col):
    count=0
    p=[]
    for k in range(256):
        for i in range(rows):
            for j in range(col):
                if(img[i,j]==k):
                    count=count+1
        p.append(count)
        count=0
    s=0
    for i in range(len(p)):
        s=s+p[i]
    for i in range(len(p)):
        p[i]=p[i]/s     #probability
    c=0
    s1=[]
    for i in range(len(p)):
        s1.append(p[i]+c)
        c=s1[i]
        s1[i]=round(s1[i]*255) #s value
    for i in range(rows):
        for j in range(col):
            r=img[i,j]
            img[i,j]=s1[r]
    return img,s1
img_dark=cv2.imread("pout-dark.jpg",0)
cv2.imshow('Original-Dark',img_dark)
cv2.waitKey(0)
rows,col=img_dark.shape
histEq(img_dark,rows,col)
cv2.imshow('Equalized',img_dark)
cv2.waitKey(0)
cv2.destroyAllWindows()
