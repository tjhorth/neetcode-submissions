class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ### Brute Force

        index = 0

        while index < len(nums): # while we have not reached end of array
            if nums[index] == val: # if element equals val
                print(f"The element {nums[index]} is equal to {val}")
                print(nums)
                for j in range(index+1, len(nums)): # shift all right elements to the left
                    nums[j-1] = nums[j]
                nums.pop()
                print(nums)
            else:
                index+=1

        return len(nums)