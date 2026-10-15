class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        ### Brute Force

        # loop through each row and check if target exists
        for row in matrix: # iterate through rows
            for elem in row: # iterate through elements
                if elem == target:
                    return True
        return False

        ### other solution
        # basically can treat each row in the matrix as a single range
        # like we coudld use the initial or last elements in each row to determine which row to search
        # then perform binary search on that row

        # Start with first element
        
        # create matrix
        # tmp = []
        # for i in len(matrix):
        #     tmp.append(matrix[i][0]) # first element in each row
        #     # 1, 10, 14
        
        # # run binary search
        # low = 0 # 1
        # high = len(tmp) - 1 # 14

        # while low < high:
        #     mid = low + ((high - low) // 2) # 1

        #     if target <= nums[mid]:
        #         high = mid # high =  =1
        #     else
        #         low = mid + 1

        


