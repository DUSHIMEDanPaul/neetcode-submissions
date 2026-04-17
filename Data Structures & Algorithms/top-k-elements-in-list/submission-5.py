class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=Counter(nums)
        return [n for n,v in result.most_common(k)]