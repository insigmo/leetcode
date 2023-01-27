# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index in range(len(nums)):
            x = target - nums[first_index]
            if x in nums and nums.index(x) != first_index:
                return [first_index, nums.index(x)]


if __name__ == '__main__':
    print(Solution().twoSum(nums=[3, 3], target=6))
