from base_types.linked_list import ListNode


def convert_list_to_list_node(lst: list) -> ListNode | None:
    if not lst:
        return None

    node = ListNode(lst[0])
    node.next = convert_list_to_list_node(lst[1:])
    return node


def convert_list_node_to_list(node: ListNode) -> list:
    lst = []

    if not node:
        return lst

    while node:
        lst.append(node.val)
        node = node.next

    return lst
