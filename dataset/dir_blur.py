import  os
import  cv2
import numpy as np


'''
0
1
2
'''
# the dir should hold the dir of imgs

imgdir = '/home/blacktea/PycharmProjects/blur/data'

def dir_blur(imglist,way=0):
    newdir=''
    if way==0:
        newdir='blur'
    elif way==1:
        newdir='gaussblur'
    elif way==2:
        newdir='median'
    else:
        newdir='runblur'

    size=[3,5,7]

    for onez in size:
        if  not os.path.exists(os.path.join(imgdir,newdir+'_size{}'.format(onez))):
            os.mkdir(os.path.join(imgdir,newdir+'_size{}'.format(onez)))
        for i,imgfile in enumerate(imglist):
            image=cv2.imread(imgfile,0)
            if way == 0:
                image=cv2.blur(image,(onez,onez))
            elif way == 1:
                image=cv2.GaussianBlur(image,(onez+2,onez+2),0)
            elif way == 2:
                #kernel=np.ones((onez-1,onez-1),np.uint8)
                #image=cv2.erode(image,kernel)
                image=cv2.medianBlur(image,onez)
            else:
                #kernel=np.ones((onez-1,onez-1),np.uint8)
                #image=cv2.dilate(image,kernel)
                image=cv2.blur(image,(onez,1))

            if  not image.shape==[]:
                #cv2.imshow('11',image)
                #cv2.waitKey(10)
                print('save',os.path.join(imgdir,newdir+'_size{}'.format(onez),'{}.jpg'.format(i)))
                cv2.imwrite(os.path.join(imgdir,newdir+'_size{}'.format(onez),'{}.jpg'.format(i)),image)



if __name__ == '__main__':

    imglist=os.listdir(os.path.join(imgdir,'src'))
    for i,imgname in enumerate(imglist):
        imglist[i]=os.path.join(imgdir,'src',imgname)


    #produce pictures
    waylist=[0,1,2,3]
    for i in waylist:
        dir_blur(imglist,i)


