# https://leetcode.com/problems/longest-common-prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        result = ''
        max_len = sorted([len(w) for w in strs])[0] - 1

        while counter <= max_len:
            if len(set(i[counter] for i in strs)) != 1:
                return result

            result += strs[0][counter]
            counter += 1

        return result


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix([""]) == ""
    assert Solution().longestCommonPrefix(["a"]) == "a"
    assert Solution().longestCommonPrefix(["ab", "a"]) == "a"
    assert Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]) == "flower"
