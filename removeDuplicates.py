def removeDuplicates(nums):
    count = 0
    for i in range(len(nums)):
        icount = nums.count(nums[i]) if nums[i]!='_' else 0
        if icount >= 1:
            count+=1
        while icount > 1: 
            nums.remove(nums[i])
            nums.append('_')
            icount-=1
    return count, nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))