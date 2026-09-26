class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)-1):
        #     max_value = max(arr[(i+1):])
        #     arr[i] = max_value
        # arr[-1] = -1
        # return arr

        # attempting solution answer - using new array

        ans = [0] * len(arr)
        max_value = -1
        for i in range(len(arr)-1, -1, -1): #start at right, increment left
            ans[i] = max_value
            max_value = max(arr[i], max_value)

        return ans

            
            