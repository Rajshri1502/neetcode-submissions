class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output=[]
        majority={}
        for i in nums:
            if i in majority:
                majority[i]+=1
            else:
                majority[i]=1    
        for i in majority:
            if majority[i]> (len(nums)//3):
                output.append(i)
        return output          