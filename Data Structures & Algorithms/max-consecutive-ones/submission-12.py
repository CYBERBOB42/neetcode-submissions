class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(len(run) for run in ''.join(map(str, nums)).split('0'))       