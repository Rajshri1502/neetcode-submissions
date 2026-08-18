class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for num in nums:
            counts[num]=counts.get(num,0) + 1
        items=counts.items()
        sorted_items=sorted(items,key= lambda pair: pair[1])
        top_pairs=sorted_items[-k:] 
        result=[pair[0] for pair in top_pairs]
        return result    