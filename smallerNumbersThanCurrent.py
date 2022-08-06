
def smallerNumbersThanCurrent(nums):
        
        smaller_num = []
        for i in range(len(nums)):
            j=0
            num = 0
            while j < len(nums):
                if nums[j] < nums[i]:
                    num +=1
                j+=1
            smaller_num.append(num)
                
        return smaller_num

print(smallerNumbersThanCurrent([8,1,2,2,3]))