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
        var=cv2.Laplacian(img,cv2.CV_64F).var()
        grou=[500,1000,1500,2000,3000,4000,5000,10000]
        for a in grou:
            if  not os.path.exists('/home/blacktea/PycharmProjects/blur/groupimgs/groups/'+str(a)):
                os.mkdir('/home/blacktea/PycharmProjects/blur/groupimgs/groups/'+str(a))
        for i in grou:
            if var<i:
                cv2.imwrite(os.path.join('/home/blacktea/PycharmProjects/blur/groupimgs/groups/'+str(i),os.path.basename(file)),img)
                break
        list_var.append(var)
        overtime=time.clock()-startime
        list_time.append(overtime)
        #print(overtime)

    list_var=np.array(list_var)
    mean=list_var.mean()

    return list_var,mean,list_time



if __name__ == '__main__':


    dir='/home/blacktea/PycharmProjects/blur/groupimgs/imges'
    list_mean=[]
    list_clock=[]

    list=os.listdir(dir)
    for i,n in enumerate(list):
        list[i]=os.path.join(dir,n)

    #print(dirimg)
    list_var,mean,sec=comput(list)
    list_mean.append(mean)
    list_clock.extend(sec)



    for i,mean in enumerate(list_mean):
        print("模糊样本测评均值 Number {}   {}:\n 清晰度：{} ".format(i,os.listdir(dir)[i],mean))

    print('平均耗时为：{}秒'.format(np.array(list_clock).mean()))
