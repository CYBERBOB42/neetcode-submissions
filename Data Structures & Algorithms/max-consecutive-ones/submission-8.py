class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        current_streak = 0
        max_val = max(len(s) for s in ''.join(map(str, nums)).split('0'))
        return max_val