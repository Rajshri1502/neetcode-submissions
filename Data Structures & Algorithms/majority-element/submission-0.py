class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        current_candidate=nums[0]
        for i in range(n):
            if count==0:
                current_candidate=nums[i]
                count+=1
            elif current_candidate==nums[i]:
                count+=1
            else:
                count-=1
        return current_candidate            