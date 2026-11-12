class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurneces of val in-place (don't use more memory)
        # return the number of elements in nums which are not equal to val
        # return this as k

        # can use another memory structure, but this is brute force and we don't necessarily change in place

        # 2 pointer, swapping end with val

        # solution 1
        length = len(nums)
        i=0
        while i < length: # Start at 0, if element is removed, do not increment. If element is not removed, move onto to next index. Length will be updated as elements are removed
            if nums[i] == val:
                j=i # start left shift at i
                while j < length-1:
                    nums[j] = nums[j+1] # shift element left
                    j+=1
                nums[length-1] = 0    
                length-=1 # decrease length by 1
                print(nums)
            else:
                i+=1
        return length

                