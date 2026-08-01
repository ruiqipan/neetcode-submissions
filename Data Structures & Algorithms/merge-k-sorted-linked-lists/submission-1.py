# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = it = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    it.next = list1
                    list1 = list1.next
                else:
                    it.next = list2
                    list2 = list2.next
                it = it.next
            it.next = list1 or list2
            return dummy.next
        if len(lists) == 0: return None
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i - 1], lists[i])
        return lists[-1]