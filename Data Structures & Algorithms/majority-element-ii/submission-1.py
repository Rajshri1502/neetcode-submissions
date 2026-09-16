class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2=0
        majority1=majority2=None
        for i in nums:
            if i==majority1:
                count1+=1
            elif i==majority2:
                count2+=1
            else:
                if count1==0:
                    majority1=i
                    count1=1
                elif count2==0:
                    majority2=i
                    count2=1
                else:
                    count1-=1
                    count2-=1
        output=[x for x in (majority1,majority2) if nums.count(x)>(len(nums)//3)]
        return output
