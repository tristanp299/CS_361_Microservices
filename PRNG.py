# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 10/03/2022
# Description: Assignment 2

from random import *

try:
    with open('prng-service.txt', 'r', encoding = 'utf-8') as f:
        filedata = f.read()

    filedata = filedata.replace('run',str(randint(0,1000)))
    with open('prng-service.txt', 'w', encoding = 'utf-8') as f:
        f.write(filedata)

except IOError:
    print("No Files exist")


