import random_data


def adjust(test,start,size):
    tmp=test[start]
    j=2*start+1
    while j<size:
        if j<size-1 and test[j]<test[j+1]:
            j+=1
        if tmp>=test[j]:
            break
        test[start]=test[j]
        start=j
        j=2*j+1
    test[start]=tmp


def buildheap(test):
    size=len(test)
    for i in range(size/2-1,-1,-1):
        adjust(test,i,size)
def heapsort(test):
    size=len(test)
    buildheap(test)
    for i in range(size-1,0,-1):
        test[i],test[0]=test[0],test[i]
        adjust(test,0,i)
    return test
