import math
def SquareMeters(area):
    sqr = []
    close = 0
    i = 1
    sum=0
    while area >= 1:
        area = area-close
        sqr.append(close)
        while i*i <= area: 
            close = i*i
            i+=1
        i=1
        sum+=close
    sqr.remove(0)
    return sqr
        

print(SquareMeters(22))