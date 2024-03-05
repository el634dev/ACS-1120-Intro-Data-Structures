#!python
from linkedlist import LinkedList

class HashTable(object):
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n^2) for n entries we need to loop through all buckets 
        then we need to loop through all bucket items to return a list of keys"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) for n entries we need to loop through all buckets 
        to return a list of all values"""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            for key, value in bucket.items():
                # Collect all values in each bucket
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) for n entries we need to loop through all buckets 
        to return a list of all items in the table"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) for n entries we need to traverse through all buckets to 
        increment the count"""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) for n entries the hash map has direct access to each pair 
        in the bucket and we can check the index or hash code"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        # Check if key-value entry exists in bucket
        if key in self.keys():
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) for n entries in the bucket we need to loop through all
        entries in the bucket to find one value associated with the given key"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # Check if key-value entry exists in bucket
        for bucket_key, bucket_value in bucket.items():
            # If found, return value associated with given key
            if bucket_key == key:
                return bucket_value
        # Otherwise, raise error to tell user get failed
        raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) for n entries we can insert of update a given key
        with its associated value without using a loop and check if the pair exists"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        buckets = self.buckets[index]

        # Check if key-value entry exists in bucket
        if index in self.keys():
            if index == key:
                # If found, update value associated with given key
                buckets[value] = buckets.update(key)
        # Otherwise, insert given key-value entry into bucket
        else:
            buckets.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) for n entries we need to loop through all pairs in
        the bucket to delete a given key from the table"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for bucket_key, bucket_value in bucket.items():
            # Check if key-value entry exists in bucket
            if bucket_key == key:
                # If found, delete entry associated with given key
                bucket.delete((bucket_key, bucket_value))
                return
        # Otherwise, raise error to tell user delete failed
        raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
