class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        diff = {}
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                diff[nums[i]]=target - nums[i]
        if target < nums[0]:
            return 0
        newDict = { key:value for (key,value) in diff.items() if value > 0}
        minValue = min(newDict.items(), key=lambda x: x[1])
        return nums.index(minValue[0]) + 1