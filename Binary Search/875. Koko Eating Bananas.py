class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            k = low + (high - low) // 2
            total_h = 0
            for pile in piles:
                total_h += math.ceil(float(pile) / k)
            if total_h <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res

                    
