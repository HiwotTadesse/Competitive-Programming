class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        containsDuplicate = False
        i = 0
        for i in nums:
            if nums.count(i) >1:
                containsDuplicate = True
                break
        return containsDuplicate