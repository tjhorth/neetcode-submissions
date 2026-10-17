class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = cnt = 0

        for num in nums:
            cnt = cnt + 1 if num == 1 else 0
            mx = max(mx, cnt)
        return mx