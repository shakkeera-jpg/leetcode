class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digit_array = [int(digit) for digit in str(n)]
        frequency={}
        res=0
        for digit in digit_array:
            if digit in frequency:
                frequency[digit]+=1
            else:
                frequency[digit]=1       
        for num,freq in frequency.items():
            res=res+(num*freq)
        return res    

                    


        