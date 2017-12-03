#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists

        # Initilalizes a hash table and set the buckets by the init size(8)
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index

        # hash() = built in python function returns the hash value of the object
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys


        # Return a list of all values in this hash table.
    def values(self):
        value_list = []
        for bucket in self.buckets:
            for entry in bucket.items():
                value_list.append(entry[1])
        return value_list

        # TODO: Running time: O(???) Why and under what conditions?
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    # Returns the total of entries in bucket
    def length(self):
        # Initialize a count of key-value entries to 0
        count = 0
        # Increases count for every value found in linkedlist

        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        for bucket in self.buckets:
            count += bucket.length()
        return count

        """Return the number of key-value entries by traversing its buckets.

        TODO: Running time: O(???) Why and under what conditions?"""
        # 0(b) Run time is relative to the number of buckets

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # TODO: Check if key-value entry exists in bucket
        if bucket.find(key) != None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # Getting the bucket index
        index = self._bucket_index(key) # Constant time
        # Getting the specific bucket from the list of buckets
        bucket = self.buckets[index] # Constant time
        # Checking if item exists in the bucket
        # Using the linked list find function.
        # Using a anonymous function to match the item to the key
        found = bucket.find(lambda item: item[0] == key) # Linear time

        # If item is found in bucket
        if found is not None:
            # Return item value
            return found[1]
        raise KeyError("Key not longer exists in this hash table")

    def set(self, key, value):

        """Insert or update the given key with its associated value"""
        # Getting the bucket index
        index = self._bucket_index(key) # Constant time
        # Getting the specific bucket from the list of buckets
        bucket = self.buckets[index] # Constant time

        # Using the contains function to check if a bucket contains the key
        if self.contains(key):
            # If it does delete it
            self.delete(key) # Linear time
        # Appending item to bucket
        self.buckets[index].append((key, value))

        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs

        # # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # TODO: Check if key-value entry exists in bucket

        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        """Delete the given key from this hash table, or raise KeyError"""
        # Getting the bucket index

        # ID
        found = bucket.find(lambda item: item[0] == key) # Linear time

        if found is not None:
            # Then delete item from bucket
            bucket.delete(found)
            return
        else:
            raise KeyError("Key not longer exists in this hash table")




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
    # ht = HashTable()
    # print(ht.buckets)
    # # ht.length()
    test_hash_table()
