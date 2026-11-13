class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = []
        total=0
        for num in nums:
            total+=num
            self.prefixes.append(total)
        print(self.prefixes)

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefixes[left-1] if left > 0 else 0
        return self.prefixes[right] - leftSum
  


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)