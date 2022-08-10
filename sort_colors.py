class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        unique_values = [0, 1, 2]
        
        elements_existance = [elem in nums  for elem in unique_values]
        empty = [0] * len(elements_existance)
        for k in range(len(elements_existance)):
            empty[unique_values[k]] = nums.count(unique_values[k]) if elements_existance[k]  else 0
        print(empty)
        j = 0
        for i in range(len(unique_values)):
            nums[j:empty[i]+j] = [i] * empty[i]
            j += empty[i]
        print(empty)