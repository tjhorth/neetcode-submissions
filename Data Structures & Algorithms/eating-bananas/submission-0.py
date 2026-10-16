class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles is an array
        # piles[i] = element in array is # of bananas in ith pile
        # integer h = numbers of hours you have to eat all the bananas in the pile
        # k = rate of eating bananas per hour
        # Each hour you may choose a pile of bananas and eat k banans from that pile. 1 pile per hour
        # if the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour

        # Return the minimum interger, k, such that you can eat all the bananas within h hours
        # k is the rate of bananas. 

        # h is the target or baseline
        
        # range we are finding is for k (rate of eating bananas per hour)
        low = 1
        high =  max(piles)
        res = high

        mid = 0
        while low <= high:
            mid = low + ((high - low) // 2)

            if self.isDoable(piles, mid, h) > 0: # too slow
                low = mid + 1
            else: # quick enough, edge towards going the rate that exceeds
                res = mid
                high = mid - 1
        return res

    def isDoable(self, piles, k, h):
        # This function will check if the eating rate will finish before h hours or not

        # this function should take the eating rate, piles, and hours and calculate the hours it would take to eat. Then compare against hours allowed

        hours_allowed = h
        # determine 
        hours_required = 0
        for pile in piles:
            time_to_eat_pile = math.ceil(float(pile) / k)
            hours_required += time_to_eat_pile

        # are hours required greater than hours allowed?
        if hours_required > hours_allowed:
            return 1
        if hours_required < hours_allowed:
            return -1
        if hours_required == hours_allowed:
            return 0

        # basically, we want to walk in the range until we get the minimum