#!python

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'

class LinkedList:
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) for n items in the list because 
        we need to loop through all n nodes to increment for each"""
        node = self.head
        count = 0

        # Loop through all nodes and count one for each
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) for n items, to append a new node we just move the 
        nodes over to create space without a loop for a new node"""
        # Create new node to hold given item
        new_node = Node(item)

        # If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        # Else append node after tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) for n items, to prepend a new node we just add
        a new node at the beginning of a list"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        Best case running time: O(1) for n items, the match could be at the beginning of the list
        Worst case running time: O(n) for n items, we need to loop through all nodes to find a match"""
        # Loop through all nodes to find item, if present return True otherwise False
        current_node = self.head

        while current_node is not None:
            if matcher(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) for n items, the item could be at the beginning of a list or the head node
        Worst case running time: O(n) for n items, we need to loop through each node to find the node to delete"""
        # Check if list is empty
        if self.is_empty():
            raise ValueError('List is empty, cannot delete from empty list')

        # Loop through all nodes to find one whose data matches given item
        current = self.head
        prev = None
        found = False

        while current is not None:
            # Update previous node to skip around node with matching data
            if current.data == item:
                found = True
                break
            # Move to the next
            prev = current
            current = current.next

        # If not found then raise a error
        if not found:
            # Otherwise raise error to tell user that delete has failed
            raise ValueError(f'Item not found: {item}')
            # Hint: raise ValueError('Item not found: {}'.format(item))

        # If the item is found, delete it by updating the pointers
        if current == self.head:
            self.head = current.next
        else:
            prev.next = current.next
        
        # Update tail if needed
        if current == self.tail:
            self.tail = prev

    def replace(self, old_item, new_item):
        """Replace self.head with new node if equal to old"""
        # Check if data is equal to old_item
        if self.head.data == old_item:
            # Create a new node with the new_item
            new_item = Node(new_item)
            # Set the next pointer of new node to the original next node
            new_item.next = self.head.next
            # Update the head to point to the newly created node
            self.head = new_item

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
