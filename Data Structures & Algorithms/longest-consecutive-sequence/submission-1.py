class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums) 
        max_seq=0
        for n in lookup:
            current_seq=1
            next_num=n+1
            if n-1 not in lookup:
                while next_num in lookup:
                    current_seq+=1
                    next_num+=1
                if current_seq>max_seq:
                    max_seq=current_seq
        return max_seq                
