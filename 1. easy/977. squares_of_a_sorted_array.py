"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/

977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_index = 0
        right_index = len(nums) - 1
        result = []

        for i in range(right_index + 1):
            left_value = nums[left_index] ** 2
            right_value = nums[right_index] ** 2
            if left_value > right_value:
                result.append(nums[left_index] ** 2)
                left_index += 1
            else:
                result.append(nums[right_index] ** 2)
                right_index -= 1

        return result[::-1]


if __name__ == '__main__':
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert Solution().sortedSquares([0]) == [0]
    assert Solution().sortedSquares([0, 1]) == [0, 1]

