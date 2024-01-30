# https://leetcode.com/problems/valid-parentheses/
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for b in s:
            if b in braces.values():
                stack.append(b)
            else:
                if not stack or stack[-1] != braces[b]:
                    return False
                stack.pop()

        return not stack


if __name__ == "__main__":
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("]") is False
    assert Solution().isValid("([)]") is False
