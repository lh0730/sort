import random_data


def mergesort(test):
    if len(test)<=1:
        return test
    mid=int(len(test)/2)
    left=mergesort(test[:mid])
    right=mergesort(test[mid:])
    return merge(left,right)


def merge(left,right):
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
