class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len=len(nums)
        ans_len=2*nums_len
        ans=nums*2
        return ans    
         