class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev=[]
        for num in range(len(nums)-1,-1,-1):
            rev.append(nums[num])
        nums=nums+rev
        return nums
