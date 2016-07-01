import random_data

def adjust(test,low,high):
    key=test[low]
    while low<high:
        while low<high and test[high]>key:
            high-=1
        while low<high and test[high]<=key:
            test[low]=test[high]
            low+=1
            test[high]=test[low]
    test[low]=key
    return low


def quicksort(test,low,high):
    if low<high:
        index=adjust(test,low,high)
        quicksort(test,low,index)
        quicksort(test,index+1,high)
    return test
