
def insertionSort1(n, arr):
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            continue
        else:
            key = arr[i+1]
            j=i
            while(j >= 0 and key < arr[j]):
                arr[j+1] = arr[j]
                print(arr)
                j+=-1
            else: 
                arr[j+1] = key
                print(arr)  

insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])