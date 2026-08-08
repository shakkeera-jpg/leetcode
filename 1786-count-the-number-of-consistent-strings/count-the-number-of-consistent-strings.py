class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        count=0
        for i in words:
            if all(char in allowed_set for char in i ):
                count+=1
        return count        
        