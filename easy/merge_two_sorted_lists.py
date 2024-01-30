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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    result = ListNode()

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     result = ListNode()
    #     while (list1 and list2) is not None:
    #         if list1.val < list2.val:
    #             result.next = list1
    #             list1.next = list1.next
    #         else:
    #             result.next = list2
    #             list2 = list2.next
    #
    #         result = result.next
    #     print(result)

    def mergeTwoLists(self, list1, list2):
        buff = ListNode()
        current = buff

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2
        return buff.next


if __name__ == "__main__":
    assert Solution().mergeTwoLists(
        list1=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None))),
        list2=ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None))),
    ) == ListNode(
        val=1,
        next=ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3, next=ListNode(
                        val=4, next=ListNode(
                            val=4, next=None
                        )
                    )
                ),
            ),
        ),
    )
    # assert Solution().mergeTwoLists(list1=[], list2=[]) == []
    # assert Solution().mergeTwoLists(list1=[], list2=[0]) == [0]
