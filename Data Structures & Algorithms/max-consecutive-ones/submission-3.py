class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ### Brute Force
        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count +=1
                if count > max:
                    max = count
            if num == 0:
                count = 0
        return max
            