def maxFrequency(nums, k):
        nums.sort()
        arrays = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                arrays.append((nums[i],(nums[j], nums[j]-nums[i])))

        print(arrays)
        dict_of_frequent = {arrays[i][1][0]:1 for i in range(len(arrays))}
        
        for i in range(len(arrays)):
            if arrays[i][1][1] <= k:
                value = dict_of_frequent.get(arrays[i][1][0])
                value+=1 
                dict_of_frequent[arrays[i][1][0]] = value
        print(dict_of_frequent)
        max_value = max(dict_of_frequent, key=dict_of_frequent.get)
        return dict_of_frequent[max_value]

maxFrequency([9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997],
7925)