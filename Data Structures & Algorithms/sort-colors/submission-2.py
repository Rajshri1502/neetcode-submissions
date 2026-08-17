class Solution:
    def sortColors(self, nums: List[int]) -> None:
        scanner=0
        first=0
        last=(len(nums)-1)
        while scanner<=last:
            if nums[scanner]==0:
                nums[scanner],nums[first]=nums[first],nums[scanner]
                scanner+=1
                first+=1
            elif nums[scanner]==1:
                scanner+=1
            else:
                nums[scanner],nums[last]=nums[last],nums[scanner]
                last-=1
                
