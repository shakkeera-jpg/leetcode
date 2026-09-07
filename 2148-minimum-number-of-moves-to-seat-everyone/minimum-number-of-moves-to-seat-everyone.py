class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted1=sorted(seats, reverse=True)
        sorted2=sorted(students, reverse=True)
        nums=0
        for i in range(len(sorted1)):
            nums += abs(sorted1[i] - sorted2[i])
        return nums        



        