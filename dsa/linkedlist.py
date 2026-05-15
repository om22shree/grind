from collections import deque, OrderedDict
import heapq
from typing import List, Dict, Tuple, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __lt__(self, other: "ListNode") -> bool:
        return self.val < other.val

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))

    dummy = ListNode()
    tail = dummy
    while heap:
        _, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


def reorder_list(head: Optional[ListNode]) -> None:
    """LeetCode 143. Mutates L0->Ln->L1->Ln-1..."""
    if not head or not head.next:
        return

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = reverse_list(slow.next)
    slow.next = None
    first = head

    while second:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next


def is_palindrome(head: Optional[ListNode]) -> bool:
    values = deque()
    while head:
        values.append(head.val)
        head = head.next

    while len(values) > 1:
        if values.popleft() != values.pop():
            return False
    return True


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = ListNode()
    tail = dummy

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next

    return dummy.next


def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before = before_tail = ListNode()
    after = after_tail = ListNode()

    while head:
        nxt = head.next
        head.next = None
        if head.val < x:
            before_tail.next = head
            before_tail = before_tail.next
        else:
            after_tail.next = head
            after_tail = after_tail.next
        head = nxt

    before_tail.next = after.next
    return before.next


class LRUCache:
    """Interview-friendly cache design using OrderedDict for O(1) operations."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class ManualLRUCache:
    """Manual DLL + hashmap version for interviewers who disallow OrderedDict."""

    class Node:
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev: Optional["ManualLRUCache.Node"] = None
            self.next: Optional["ManualLRUCache.Node"] = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, ManualLRUCache.Node] = {}
        self.left = self.Node()
        self.right = self.Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: "ManualLRUCache.Node") -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_mru(self, node: "ManualLRUCache.Node") -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self._insert_mru(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3])
    assert to_list(reverse_list(head)) == [3, 2, 1]
    assert has_cycle(build_linked_list([1, 2, 3])) is False
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
