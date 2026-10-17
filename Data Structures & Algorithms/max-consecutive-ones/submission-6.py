class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = cnt = 0

        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
            mx = max(cnt, mx)
        return mx