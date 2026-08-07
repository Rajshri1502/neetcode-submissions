class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originals=set(nums)
        return len(originals)!=len(nums)            

