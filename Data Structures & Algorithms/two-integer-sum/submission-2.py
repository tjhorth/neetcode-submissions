class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each num, calculate the difference between the target and num. Store key as difference, and index as value
        # If difference is found between another index, returnindicies

        map = {}

        for i in range(len(nums)):
            diff = target-nums[i] #7-3=4
            if diff in map: #if 4 in map
                return [min(map[diff], i), max(map[diff], i)]
            else:
                map[nums[i]] = i # 3 --> 0
            
