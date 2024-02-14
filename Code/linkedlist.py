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
        if self.head is not None:
            return True
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) Why and under what conditions?"""
        count = 0
        node = self.head

        # Loop through all nodes and count one for each
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        new_node = Node(item)
        # If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() is True:
            self.head = new_node
            self.tail = new_node
        # Else append node after tail
        else:
            self.tail.next = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.is_empty() is not False:
            self.head = new_node
        new_node.next = self.head

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find item, if present return True otherwise False
        current_node = self.head

        while current_node is not None:
            if current_node == matcher:
                current_node = current_node.next
                return True
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item
        current_node = self.head

        while self.head is not None:
            # Update previous node to skip around node with matching data
            if current_node.data.prev == item: 
                return True
            else:
                current_node = None
                current_node = current_node.next
            # Otherwise raise error to tell user that delete has failed
            raise Exception('Deletion has failed')
        raise ValueError(f'Item not found: {item}')
        # Hint: raise ValueError('Item not found: {}'.format(item))


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
