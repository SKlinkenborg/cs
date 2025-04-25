'''
You can visualize it as a line at a deli:

    The customer at the front of the line (equivalent to the head in a queue) is the first customer to get served
    Any new customer must go to the back of the line (the tail of the queue) and wait until everyone in front of them 
    has been served (no line cutters allowed in this deli!)
    The deli
    Preview: Docs Loading link description
    server
    only needs to know about the current order

Now, we can use Python to build out a Queue class with those three essential queue methods:

    enqueue() which will allow us to add a new node to the tail of the queue
    dequeue() which will allow us to remove a node from the head of the queue and return its value
    peek() which will allow us to view the value of head of the queue without returning it

We’ll also set up a few helper methods that will help us keep track of the queue size in order to prevent queue “overflow” and “underflow.”
'''

from node import Node
# Create the Queue class below:
class Queue:
    def __init__(self, max_size = None, size = 0):
        self.head = None
        self.tail = None
        # Next 2 were added for Bounded Queue creation
        self.max_size = max_size
        self.size = size
    '''
    “Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue()
    Preview: Docs A method is a small piece of code, usually defined in a class, that can be used outside the class and in other parts of the program.
    method. There are three scenarios that we are concerned with when adding a node to the queue:
        The queue is empty, so the node we’re adding is both the head and tail of the queue
        The queue has at least one other node, so the added node becomes the new tail
        The queue is full, so the node will not get added because we don’t want queue “overflow”
    '''
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print('Adding ' + str(item_to_add.get_value()) + ' to the queue!')
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
    '''
    Like enqueue(), we care about the size of the queue — but in the other direction, so that we prevent queue “underflow”. After all, you don’t want to remove something that isn’t there!
    As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), dequeue() will also remove the current head and replace it with the following node.

    For dequeue, there are three scenarios that we will take into account:

    The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
    The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s head and tail to None
    The queue has more than one node, and we just remove the head node and reset the head to the following node
    '''
    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(item_to_remove.get_value())
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")    

    def peek(self):
        # Make sure there's a value to show
        if self.size > 0:
            return self.head.get_value()
        else:
            print("Nothin left to serve boss")
  
    # Add Bounded Queue support
    # This requires 2 new properties: size of list currently, and max_size
    # And 3 methods: get_size() of current list, has_space() return True if not full, is_empty() returns true if list empty

    # Create a method to check the current list size
    def get_size(self):
        return self.size
    
    # Create a method to check if the queue is full
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    # Create a method to check if the queue is empty
    def is_empty(self):
        if self.get_size() == 0:
            return True
        
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #