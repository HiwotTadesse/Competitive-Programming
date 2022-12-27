def GuthrieIndex(n):
    count = 0
    if n == 1:
        return count
    else:
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = n*3+1
            count+=1
        return count
            
        
            
            
print(GuthrieIndex(42))