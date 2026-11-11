class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # brute force
        count=0
        mx = 0
        for num in nums:
            if num == 1:
                count+=1
                mx = max(count, mx)
            else:
                count=0
        return mx
