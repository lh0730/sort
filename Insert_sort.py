import random_data

def Insert(test):
    i=1
    for i in range(1,len(test)):
        j=i
        while j > 0 and test[j-1]>test[i]:
            j=j-1
        test.insert(j,test[i])
        test.pop(i+1)
    return test
