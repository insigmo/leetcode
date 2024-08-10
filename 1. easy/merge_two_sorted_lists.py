# https://leetcode.com/problems/merge-two-sorted-lists/
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

from base_types.linked_list import ListNode
from converters import convert_list_to_list_node, convert_list_node_to_list


class Solution:
    result = ListNode()

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    l1 = convert_list_to_list_node([1, 2, 4])
    l2 = convert_list_to_list_node([1, 3, 4])
    expected = [1, 1, 2, 3, 4, 4]
    actual = convert_list_node_to_list(Solution().mergeTwoLists(l1, l2))
    assert actual == expected, f"{actual} != {expected}"

    l1 = convert_list_to_list_node([])
    l2 = convert_list_to_list_node([])
    expected = []
    actual = convert_list_node_to_list(Solution().mergeTwoLists(l1, l2))
    assert actual == expected, f"{actual} != {expected}"

    l1 = convert_list_to_list_node([])
    l2 = convert_list_to_list_node([0])
    expected = [0]
    actual = convert_list_node_to_list(Solution().mergeTwoLists(l1, l2))
    assert actual == expected, f"{actual} != {expected}"
