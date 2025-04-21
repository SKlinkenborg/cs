'''
Node Implementation
10 min

Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.

Remember that a node contains two elements:

    data
    a link to the next node
'''

# Define your Node class below:
# A Node consists of a value, and links to other node(s)
class Node:
    def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node
    # allows us to call the Node's value
    def get_value(self):
     return self.value
    # allows us to call the Node's next_node
    def get_next_node(self):
      return self.next_node
    # allows us to set the Node's next_node
    def set_next_node(self, next_node):
      self.next_node = next_node

# my_node = Node(44)
# print(my_node.get_value())

'''
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

For our use, we want to be able to:
    - get the head node of the list (it’s like peeking at the first item in line) = .get_head_node()
    - add a new node to the beginning of the list = .insert_beginning()
    - print out the list values in order
    - remove a node that has a particular value
'''

# Create your LinkedList class below:
class LinkedList:
    
    # When we create a LinkedList, create a head node for it using the Node class
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    # allows us to retrieve the head_node value
    def get_head_node(self):
        return self.head_node
    
    # allows us to insert a new head node at the beginning of the LinkedList
    def insert_beginning(self, new_value):
       # create a new node after the head_node
       new_node = Node(new_value)
       # copy the value from the current head_node into the next node
       new_node.set_next_node(self.head_node)
       # now set the new_node as the head_node
       self.head_node = new_node
    
    # allows us to print out a string representation of a list's nodes' values.
    def stringify_list(self):
        string_list = ""
        # pop the head node into the variable current_node
        current_node = self.get_head_node()
        while current_node:
            # if the node's value is None, it is the last item in the list
            if current_node.get_value() != None:
                # get the node's value and add it
                string_list += str(current_node.get_value()) + "\n"
            # pop the next node in the variable current_node. When we run out (returns False), continue    
            current_node = current_node.get_next_node()
        return string_list


        '''
        The final use case we mentioned was the ability to remove an arbitrary node with a particular value. This is slightly more complex, since a couple of special cases need to be handled.

        Consider the following list:

        a -> b -> c

        If node b is removed from the list, the new list should be:

        a -> c

        We need to update the link within the a node to match what b was pointing to prior to removing it from the linked list.

        Lucky for us, in Python, nodes which are not referenced will be removed for us automatically. If we take care of the references, b will be “removed” for us in a process called Garbage Collection.

        For the purposes of this lesson, we’ll create a function that removes the first node that contains a particular value. However, you could also build this function to remove nodes by
        Preview: Docs Loading link description
        index
        or remove all nodes that contain a particular value.
        '''
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
        
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())