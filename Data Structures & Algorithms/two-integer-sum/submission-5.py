class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 1. brute force is iterate through nested loops
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # 2. 2 pointer (walk in to indices)
        # 3. hash map
        seen = {} # key is difference, value is index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [min(i, seen[diff]), max(i, seen[diff])]
            else:
                seen[nums[i]]=i


