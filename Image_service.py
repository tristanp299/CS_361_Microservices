# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 10/03/2022
# Description:
import os
import time

with open('image-service.txt', 'r') as f:
    num = f.readline()
    num = int(num)
    imgs = os.listdir(path = './Images/archive/')
    image = imgs[num%(len(imgs)-1)]
with open('image-service.txt', 'w') as f:
    f.write('')
    time.sleep(1)
    f.write('./Images/archive/' +image)
