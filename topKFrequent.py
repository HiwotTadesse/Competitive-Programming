class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {};
        for i in nums:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        sorted_list = sorted(result.items(), key= lambda kv:kv[1], reverse=True)
        return [i[0] for i in sorted_list[0:k]]
