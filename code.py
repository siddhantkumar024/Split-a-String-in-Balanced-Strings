class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b=0
        bc=0
        for nu in s:
            if nu=='L':
                b+=1
            elif nu=='R':
                b-=1
            if b==0:
                bc+=1
        return bc
        
