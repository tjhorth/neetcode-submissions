class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = set()

        for num in nums:
            if num in countMap:
                return True
            countMap.add(num)
        return False