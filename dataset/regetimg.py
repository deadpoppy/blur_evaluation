import os
import cv2

if __name__ == '__main__':


    src='/home/blacktea/PycharmProjects/blur/dataset/srcdata'
    savedir='/home/blacktea/PycharmProjects/blur/dataset/imges'
    dirnames=os.listdir(src)
    numpictures=0
    for dirna in dirnames:
        for name in os.listdir(os.path.join(src,dirna)):
            img=cv2.imread(os.path.join(src,dirna,name))
            numpictures=numpictures+1
            cv2.imwrite(os.path.join(savedir,str(numpictures))+'.jpg',img)

