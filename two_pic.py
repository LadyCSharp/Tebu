import os
import random
from PIL import Image                                                                                
#import matplotlib.pyplot as plt
def some_pic(path, count):
    k=0
    for p in os.walk(path):
        for q in p[2]:
            if q.split('.')[-1]=='jpg':
                if random.random()<0.1:
                    print (q)
                    #os.startfile(p[0]+'\\'+q)
                    #image = plt.imread(p[0]+'\\'+q)
                    #plt.imshow(image)
                    img = Image.open(p[0]+'\\'+q)
                    img.show()
                    k+=1
            if k>=count:
                return
        