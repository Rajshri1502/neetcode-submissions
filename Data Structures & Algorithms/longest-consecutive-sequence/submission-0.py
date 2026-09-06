class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums) 
        max_seq=0
        for n in lookup:
            current_seq=1
            next_num=n+1
            if n-1 not in lookup:
                for i in range(len(lookup)):
                    if next_num in lookup:
                        next_num+=1
                        current_seq+=1
            if current_seq>max_seq:
                max_seq=current_seq                        
        return max_seq                