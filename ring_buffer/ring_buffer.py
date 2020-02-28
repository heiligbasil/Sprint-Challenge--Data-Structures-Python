from doubly_linked_list import DoublyLinkedList

"""A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, 
the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for 
use cases such as storing logs and history information, where you typically want to store information up until it reaches a 
certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data. Implement this 
behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. 
The get method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not 
return any None values in the list even if they are present in the ring buffer. """


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.storage.length > 0:
            refreshed_node = self.storage.head
            while refreshed_node:
                list_buffer_contents.append(refreshed_node.value)
                refreshed_node = refreshed_node.next
        return list_buffer_contents


buffer = RingBuffer(3)
print(buffer.get())  # should return []
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())  # should return ['a', 'b', 'c']
# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
print(buffer.get())  # should return ['d', 'b', 'c']
buffer.append('e')
buffer.append('f')
print(buffer.get())  # should return ['d', 'e', 'f']


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
