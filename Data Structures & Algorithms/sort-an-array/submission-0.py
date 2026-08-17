class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(list1: List[int],list2: List[int]) -> List[int]:
            i=0
            j=0
            merged=[]
            while i<len(list1) and j<len(list2):
                if list1[i]<list2[j]:
                    merged.append(list1[i])
                    i+=1
                else:
                    merged.append(list2[j])
                    j+=1
            if i<len(list1):
                merged.extend(list1[i:])
            if j<len(list2):
                merged.extend(list2[j:])
            return merged
        def merge_sort(list1: List[int]) -> List[int]:
            if len(list1)<=1:
                return list1
            list2=list1[(len(list1))//2:]    
            list1=list1[0:(len(list1))//2]
            sorted_l1=merge_sort(list1)
            sorted_l2=merge_sort(list2)
            return merge(sorted_l1,sorted_l2)
        return merge_sort(nums)       