class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_number = min(nums)
        missing=0
        for i in range(min_number, len(nums)+1):
            if i not in nums:
                missing = i
        return missing
