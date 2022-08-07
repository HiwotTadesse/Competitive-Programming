def targetIndices(nums, target):
        for i in range(len(nums)):
            j=i+1
            while j < len(nums):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j] 
                    nums[j] = temp
                j+=1
        target_nums = []
        for j in range(len(nums)):
            if nums[j] == target:
                target_nums.append(j)
        return target_nums


print(targetIndices([1,2,5,2,3], 2))