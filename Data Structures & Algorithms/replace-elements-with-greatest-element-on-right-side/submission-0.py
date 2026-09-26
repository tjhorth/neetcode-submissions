class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # have to start from 0 and work right
        for i in range(len(arr)-1):
            max_value = max(arr[(i+1):])
            arr[i] = max_value
        arr[-1] = -1
        return arr
            
            