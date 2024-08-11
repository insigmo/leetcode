"""
https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional

from base_types.linked_list import ListNode
from converters import convert_list_node_to_list, convert_list_to_list_node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


if __name__ == '__main__':
    lst = convert_list_to_list_node([1, 2, 3, 4, 5])
    expected = [5, 4, 3, 2, 1]
    actual = convert_list_node_to_list(Solution().reverseList(lst))
    assert actual == expected, f"{actual} != {expected}"


    lst = convert_list_to_list_node([1,2])
    expected = [2, 1]
    actual = convert_list_node_to_list(Solution().reverseList(lst))
    assert actual == expected, f"{actual} != {expected}"


    lst = convert_list_to_list_node([])
    expected = []
    actual = convert_list_node_to_list(Solution().reverseList(lst))
    assert actual == expected, f"{actual} != {expected}"
