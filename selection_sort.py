def selectionSort(arr,n):
        for i in range(n):
            j=i+1
            while j < n:
                if arr[j] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j] 
                    arr[j] = temp
                j+=1

selectionSort( [4, 1, 3, 9, 7 ],5)