class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for x in strs:
            new=''.join(sorted(x))
            result[new].append(x)
        return list(result.values())