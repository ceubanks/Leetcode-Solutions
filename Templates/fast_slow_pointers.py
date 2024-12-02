from typing import Optional, Any

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class FastSlowPointers:
    """
    A collection of fast & slow pointer pattern implementations.
    Used for problems involving linked lists or arrays where we need to find
    cycles or middle elements.
    """
    
    @staticmethod
    def find_cycle(head: Optional[ListNode]) -> bool:
        """
        Template for cycle detection in linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            True if cycle exists, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return False
            
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False
    
    @staticmethod
    def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Template for finding start of cycle in linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            Node where cycle begins, or None if no cycle
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return None
            
        # Find meeting point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Move one pointer to head and advance both by one
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None
    
    @staticmethod
    def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Template for finding middle of linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            Middle node of the list
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return None
            
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

# Example usage
if __name__ == "__main__":
    # Create a linked list with cycle
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next  # Create cycle
    
    print("Has cycle:", FastSlowPointers.find_cycle(head))
    cycle_start = FastSlowPointers.find_cycle_start(head)
    print("Cycle starts at value:", cycle_start.val if cycle_start else None)
    
    # Create a normal linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    middle = FastSlowPointers.find_middle(head)
    print("Middle value:", middle.val if middle else None) 