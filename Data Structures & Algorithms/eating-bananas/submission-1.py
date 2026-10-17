class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # if time_required is greater than h, then rate is too slow
        # otherwise it's acceptable, but we want to find the minimum rate (worst performance)
        
        low = 1 # minimum rate per hour is 1
        high = max(piles) # maximum rate per hour is the size of the largets pile
        ans = high # default answer is equivalent to high
        
        while low <= high: # walk in range until we find the last acceptable answer
            mid = low + ((high - low) // 2) # use binary search

            # determine time required with new rate (mid)
            time_required = 0
            for elem in piles:
                time_required = time_required + math.ceil(elem/mid)
            
            if time_required > h: # rate is too slow, needs to be increased
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans

        # there will always be an acceptable answer, so no need to handle outside of return the answer
