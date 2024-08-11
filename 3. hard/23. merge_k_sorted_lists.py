"""
https://leetcode.com/problems/merge-k-sorted-lists

23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from typing import List, Optional

from base_types.linked_list import ListNode
from converters import convert_list_to_list_node, convert_list_node_to_list


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            len_list = len(lists)
            for i in range(0, len_list, 2):
                l1 = lists[i]
                next_index = i + 1
                l2 = lists[next_index] if next_index < len_list else None
                new_list = self.mergeTwoLists(l1, l2)
                merged_lists.append(new_list)

            lists = merged_lists

        return lists[0]

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
    lst = list(map(convert_list_to_list_node, [[1, 4, 5], [1, 3, 4], [2, 6]]))
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    actual = convert_list_node_to_list(Solution().mergeKLists(lst))
    assert actual == expected, f"{actual} != {expected}"

    lst = list(map(convert_list_to_list_node, []))
    expected = []
    actual = convert_list_node_to_list(Solution().mergeKLists(lst))
    assert actual == expected, f"{actual} != {expected}"

    lst = list(map(convert_list_to_list_node, [[]]))
    expected = []
    actual = convert_list_node_to_list(Solution().mergeKLists(lst))
    assert actual == expected, f"{actual} != {expected}"
