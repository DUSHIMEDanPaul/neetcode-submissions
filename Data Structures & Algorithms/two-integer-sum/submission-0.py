class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         array=nums
         seen={}
         t=target
         for i in range(len(array)):
            current=array[i]
            complement=t-current
            if complement in seen:
              return [seen[complement],i]  
            else:
              seen[current]=i
         return 'not found'
       
                