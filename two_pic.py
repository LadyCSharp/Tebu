import os
import random
                                                                              
import matplotlib.pyplot as plt
def some_pic(path, count):
    k=0
    for p in os.walk(path):
        for q in p[2]:
            if q.split('.')[-1]=='jpg':
                if random.random()<0.1:
                    print (q)
                    img=plt.imread(p[0]+'\\'+q)
                    plt.imshow(img)
                    plt.show()
                   
                   
                    k+=1
            if k>=count:
                return
        