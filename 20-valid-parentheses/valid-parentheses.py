class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={")":"(" , "}":"{" , "]":"["}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or pairs[ch] != stack.pop():
                    return False
        return len(stack)==0             


        