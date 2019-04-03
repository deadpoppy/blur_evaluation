import os
import cv2
import time
import numpy as np


def comput(list):
    list_var=[]
    list_time=[]
    for file in list:

        img=cv2.imread(file,0)
        startime = time.clock()
        #img=cv2.GaussianBlur(img,(3,3),0)
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
        var=cv2.Laplacian(img,cv2.CV_64F).var()
        #img=cv2.convertScaleAbs(img)
        list_var.append(var)
        overtime=time.clock()-startime
        list_time.append(overtime)
        #print(overtime)

    list_var=np.array(list_var)
    mean=list_var.mean()

    return list_var,mean,list_time



if __name__ == '__main__':


    dir='/home/blacktea/PycharmProjects/blur/data'
    list_mean=[]
    list_clock=[]
    for dirimg in os.listdir(dir):
        list=os.listdir(os.path.join(dir,dirimg))
        for i,n in enumerate(list):
            list[i]=os.path.join( os.path.join(dir,dirimg),n)

        #print(dirimg)
        _,mean,sec=comput(list)
        list_mean.append(mean)
        list_clock.extend(sec)



    for i,mean in enumerate(list_mean):
        print("模糊样本测评均值 Number {}   {}:\n 清晰度：{} ".format(i,os.listdir(dir)[i],mean))

    print('平均耗时为：{}秒'.format(np.array(list_clock).mean()))
