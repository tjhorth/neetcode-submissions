class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []

        for elem in nums:
            if elem == val:
                continue
            else:
                tmp.append(elem)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)