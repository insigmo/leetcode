"""
https://leetcode.com/problems/add-two-numbers

2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
from typing import Optional

from base_types.linked_list import ListNode
from converters import convert_list_to_list_node, convert_list_node_to_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (l1 and l2):
            return None

        dummy = ListNode()
        tail = dummy
        increment = 0

        while l1 or l2:
            a = 0
            b = 0

            if l1:
                a = l1.val
                l1 = l1.next

            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + increment
            increment = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

        if increment:
            tail.next = ListNode(increment)

        return dummy.next


if __name__ == '__main__':
    l1 = convert_list_to_list_node([2, 4, 3])
    l2 = convert_list_to_list_node([5, 6, 4])
    expected = [7, 0, 8]
    actual = convert_list_node_to_list(Solution().addTwoNumbers(l1, l2))
    assert actual == expected, f"{actual} != {expected}"

    l1 = convert_list_to_list_node([0])
    l2 = convert_list_to_list_node([0])
    expected = [0]
    actual = convert_list_node_to_list(Solution().addTwoNumbers(l1, l2))
    assert actual == expected, f"{actual} != {expected}"

    l1 = convert_list_to_list_node([9, 9, 9, 9, 9, 9, 9])
    l2 = convert_list_to_list_node([9, 9, 9, 9])
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    actual = convert_list_node_to_list(Solution().addTwoNumbers(l1, l2))
    assert actual == expected, f"{actual} != {expected}"
