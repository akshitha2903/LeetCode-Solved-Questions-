class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = (high-low) // 2
        if low%2 == 0 and high%2 == 0:
            return length
        return length+1
        