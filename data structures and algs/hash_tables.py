from linked_list import LinkedList

class ChainHash:
    def __init__(self, hash_fn, max_size):
        self.table = [LinkedList() for _ in range(max_size)]
        self.size = 0
        self.hash_fn = hash_fn

    def has_key(self, key):
        index = self.hash_fn(key)
        return self.table[index].find(key) is not None

    def insert(self, key):
        index = self.hash_fn(key)
        # Make sure that key is not already in the table
        if not self.table[index].find(key):
            self.table[index].insert(key)
            self.size += 1

    def delete(self, key):
        index = self.hash_fn(key)
        node = self.table[index].find(key)
        if node:
            self.table[index].delete(node)
            self.size -= 1

    def get_size(self):
        return self.size

    def __str__(self):
        table_str = [f"{i}: {str(self.table[i])}" for i in range(len(self.table))]
        return "\n".join(table_str)


class OpenHash:
    sentinel = object()  # tombstone

    def __init__(self, hash_fn, max_size):
        self.table = [None] * max_size
        self.size = 0
        self.hash_fn = hash_fn

    def has_key(self, key):
        index = self.hash_fn(key)
        #print("original index: ", index)
        original_index = index

        while self.table[index] is not None: # and self.table[index] != self.sentinel:
            #print("current index: ", index)
            if self.table[index] == key:
                return True  # key found

            index = (index + 1) % len(self.table)

            # Check if we have cycled back to original index
            if index == original_index:
                break

        return False

    def insert(self, key):
        index = self.hash_fn(key)
        original_index = index

        if self.has_key(key) is False:
            # Check for None values and if key already exists in table
            while self.table[index] is not None and self.table[index] != self.sentinel:
                index = (index + 1) % len(self.table)

                # Check if we have cycled back to original index
                if index == original_index:
                    # Table is full, exit the insert
                    return
                    
            self.table[index] = key
            self.size += 1

    def delete(self, key):
        index = self.hash_fn(key)
        original_index = index

        while self.table[index] is not None:
            # If we have found the key
            if self.table[index] == key:
                self.table[index] = self.sentinel  # Mark as a tombstone
                self.size -= 1
                return
            index = (index + 1) % len(self.table)

            # Check if we have cycled back to the original index
            if index == original_index:
                break

    def get_size(self):
        return self.size

    def __str__(self):
        table_str = [f"{i}: {str(self.table[i])}" for i in range(len(self.table))]
        return "\n".join(table_str)
