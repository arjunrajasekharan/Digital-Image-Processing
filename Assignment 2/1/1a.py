class Mat:
    def __init__(self,row,col):
        self.row=row
        self.col=col

class Index:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def func(value,beg,end):
    if value<beg:
        return beg
    elif value>=beg and value<=end:
        return value
    else:
        return end

def overlap(
        mat_size=Mat(4,4),
        filter_size=Mat(3,3),
        filter_center=Index(1,1),
        matrix_index=Index(0,0)
    ):
    local=[]
    for i in range(
            func(0-filter_center.x+matrix_index.x,0,mat_size.row),
            func(filter_size.row-1-filter_center.x+matrix_index.x+1,0,mat_size.row)
        ):
        for j in range(
                func(0-filter_center.y+matrix_index.y,0,mat_size.col),
                func(filter_size.col-1-filter_center.y+matrix_index.y+1,0,mat_size.col)
            ):
            # print((i,j),end=",")
            local.append((i,j))
        # print()
    return local

def average_filtering(img,filter_size=Mat(3,3),filter_center=Index(1,1)):
    row,col,ch=img.shape
    print("Shape ",img.shape)
    filter_area=filter_size.row*filter_size.col
    img_copy=img.copy()
    for i in range(row):
        for j in range(col):
            overlap_indexes=overlap(Mat(row,col),filter_size,filter_center,Index(i,j))
            local_pixel=[0 for i in range(ch)]
            for x,y in overlap_indexes:
                for k in range(ch):
                    local_pixel[k]+=img[x][y][k]/filter_area
            for k in  range(ch):
                # local_pixel[k]/=len(overlap_indexes)
                img_copy[i][j][k]=local_pixel[k]
        print("Current location : ",i,j,end="\r")
    print()
    return img_copy

def debug():
    img=mpimg.imread("./lena.jpg")
    img_noisy=random_noise(img, mode='s&p',amount=0.5)
    # print(img[0][0])
    # filter=[[0 for i in range(3)] for j in range(3)]

    # mat=[# 6 x 6 matrix
    #     [1,2,3,12,13,14],
    #     [4,5,6,23,24,25],
    #     [7,8,9,34,35,36],
    #     [1,2,3,12,13,14],
    #     [4,5,6,23,24,25],
    #     [7,8,9,34,35,36],
    # ]
    # correlation_on(mat,filter,[1,1])
    # print( overlap(Mat(5,5),Mat(3,3),Index(1,1),Index(0,1)) )
    img_avg=average_filtering(img_noisy,Mat(3,3),Index(1,1))
    plt.imshow(img_noisy)
    plt.savefig("q11_output/noisy_output.jpg")
    plt.imshow(img_avg)
    plt.savefig("q11_output/avg_output.jpg")
    multishow(1,3,img,img_noisy,img_avg)

def multishow(rows=1,columns=1,*all_images):
    for i in range(len(all_images)):
        plt.subplot(rows,columns,i+1)
        plt.axis("off")
        plt.title("Image "+str(i+1))
        plt.imshow(all_images[i])
    plt.show()

def main():
    img=mpimg.imread("./lena.jpg")
    lena_img_noise_level=[]
    for i in range(1,10+1):
        lena_img_noise_level.append(random_noise(img, mode='s&p',amount=i/10))
    plt.figure(figsize=(10,5),dpi=150)
    for i in range(1,10+1):
        plt.subplot(2,5,i)
        plt.axis("off")
        plt.title("Image Noise\nLevel "+str(i)+"/10")
        plt.imshow(lena_img_noise_level[i-1])
    plt.savefig("noise_level_output.jpg")
    # print("Noisy Images")
    plt.show()
    
    img_noisy=lena_img_noise_level[5]
    plt.imshow(img_noisy)
    plt.savefig("noisy_output.jpg",dpi=300)

    img_avg_3x3=average_filtering(img_noisy,Mat(3,3),Index(1,1))
    plt.imshow(img_avg_3x3)
    plt.savefig("avg_3x3_output.jpg",dpi=300)
    
    img_avg_5x5=average_filtering(img_noisy,Mat(5,5),Index(1,1))
    plt.imshow(img_avg_5x5)
    plt.savefig("avg_5x5_output.jpg",dpi=300)
    
    img_avg_7x7=average_filtering(img_noisy,Mat(7,7),Index(1,1))
    plt.imshow(img_avg_7x7)
    plt.savefig("avg_7x7_output.jpg",dpi=300)
    
    multishow(1,5,img,img_noisy,img_avg_3x3,img_avg_5x5,img_avg_7x7)

if (__name__=="__main__"):
    from skimage.util import random_noise
    from matplotlib import pyplot as plt,image as mpimg
    main()
    # debug()
