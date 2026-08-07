class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        result=[]
        for idx,val in enumerate(nums):
            j=target-val
            if j in indices:
                return [indices[j],idx]
            indices[val]=idx    