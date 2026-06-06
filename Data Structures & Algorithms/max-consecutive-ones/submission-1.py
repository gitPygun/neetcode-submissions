class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        max_count = 0

        for i in nums:
            if i == 1:
                cur += 1

                if cur > max_count:
                    max_count = cur

            else:
                cur = 0

        return max_count


