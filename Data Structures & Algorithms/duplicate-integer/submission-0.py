class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for num in nums:
            if num in countMap:
                return True
            else:
                countMap[num] = num
        return False