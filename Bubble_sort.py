import random_data

def Bubble(test):
    l=len(test)-2
    i=0
    while i<=l:
        j=l
        while j>=i:
            if test[j+1]<test[j]:
                test[j],test[j+1]=test[j+1],test[j]
            j=j-1
        i=i+1
    return test
