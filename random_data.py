from numpy import random


def getdata(num):
    test=[]
    i=0
    for i in range(0,num):
        test.append(random.randint(0,10000))
    return test

