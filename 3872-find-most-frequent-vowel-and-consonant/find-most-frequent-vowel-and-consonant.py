class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['a', 'e', 'i', 'o','u']
        c1={}
        c2={}
        for i in s:
            if i in vowels:
                if i in c1:
                   c1[i]=c1.get(i, 0) + 1
                else:
                    c1[i]=1
            else:
                if i in c2:
                    c2[i]=c2.get(i, 0) + 1
                else:
                    c2[i]=1
        maxvalue1=max(c1.values(), default=0)
        maxvalue2=max(c2.values(), default=0) 
        return maxvalue1+maxvalue2           

                
            
            
                                 
