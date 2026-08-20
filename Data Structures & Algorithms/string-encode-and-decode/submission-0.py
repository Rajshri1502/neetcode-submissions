class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            encoded=str(len(word))+"#"+word
            result+=encoded
        return result    

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            hash_pos=s.find('#',i)
            length=int(s[i:hash_pos])
            result.append(s[hash_pos+1:hash_pos+1+length])
            i=hash_pos+1+length
        return result       