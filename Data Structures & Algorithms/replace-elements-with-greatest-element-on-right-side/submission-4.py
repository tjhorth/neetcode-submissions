class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        
        for i in range(len(arr)-2, -1, -1): # traverse from right to left
            tmp = arr[i]
            arr[i] = mx
            mx = max(mx, tmp)
        arr[-1] = -1
        return arr
