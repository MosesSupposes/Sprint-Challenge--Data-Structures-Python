from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None:
            self.current = self.storage.head

        if len(self.storage) == self.capacity:
            next_current = self.current.next
            self.current.insert_after(item)
            self.storage.delete(self.current)
            self.current = next_current
            # next_current = self.current.next
            # self.current.delete()
            # self.storage.add_to_head(item)
            # self.current = next_current
        else:
            self.storage.add_to_tail(item)

 
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next            

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
