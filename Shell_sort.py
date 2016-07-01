import random_data

def Shell(test):
    dist=len(test)/2
    while dist>0:
        for i in range(dist,len(test)):
            tmp=test[i]
            j=i
            while j>=dist and tmp<test[j-dist]:
                test[j]=test[j-dist]
                j-=dist    
            test[j]=tmp
        dist=dist/2
    return test


