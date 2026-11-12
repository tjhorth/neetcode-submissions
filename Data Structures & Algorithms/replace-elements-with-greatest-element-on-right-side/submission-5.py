class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # replace every element in arr with the greatest element among the elements to its right
        # replace last element with -1
        # return the array

        mx = arr[-1]

        for i in range(len(arr)-1, -1, -1): # start 2nd to last on right and work left
            tmp = arr[i] # store current value

            arr[i] = mx

            # update new mx for next element. keeping track of max
            mx = max(mx, tmp)
        
        arr[-1] = -1
        return arr