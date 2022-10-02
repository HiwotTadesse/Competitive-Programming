class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndex =[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   targetIndex.append(i)
                   targetIndex.append(j)
        return  targetIndex