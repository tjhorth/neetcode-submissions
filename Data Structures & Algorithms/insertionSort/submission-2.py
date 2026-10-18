# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        ans.append(pairs[:])

        if not pairs:
            return []
        
        for i in range(1, len(pairs)): # iterate through 2nd elem to end (first is already sorted)
            # above for loop will be the index of the number we are checking
            for j in range(i, 0, -1): # loop from current index to the left all the way to start
                print(pairs[j].key < pairs[j-1].key)
                if pairs[j].key < pairs[j-1].key:
                    tmp = pairs[j-1]
                    pairs[j-1] = pairs[j]
                    pairs[j] = tmp
                else:
                    break 

            ans.append(pairs[:])

        return ans

            