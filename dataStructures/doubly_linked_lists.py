'''

'''

'''
The difference between a doubly linked list and a singly linked list is that in a doubly linked list, the nodes have pointers to the previous node as well as the next node. This means that the doubly linked list data structure has a tail property in addition to a head property, which allows for traversal in both directions.

So the nodes we will use for our doubly linked list contain three elements:

    A value
    A pointer to the previous node
    A pointer to the next node

Depending on the end-use of the doubly linked list, there are a variety of methods that we can define.

For our use, we want to be able to:

    Add a new node to the head (beginning) of the list
    Add a new node to the tail (end) of the list
    Remove a node from the head of the list
    Remove a node from the tail of the list
    Find and remove a specific node by its value
    Print out the nodes in the list in order from head to tail
'''

class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  # Add a new Node to the beginning (head) of the doubly list
  def add_to_head(self, new_value):
    # Create a new head node
    new_head = Node(new_value)
    # Check if there's a current head.
    current_head = self.head_node
    if current_head != None:
      # If there is an old head, set the prev_node to the new head
      current_head.set_prev_node(new_head)
      # And set the next_node of the new head to the old head
      new_head.set_next_node(current_head)
    # Now set the new head node value to head_node
    self.head_node = new_head
    # Check if there's a tail_node. If not, set the tail_node to the head_node
    current_tail = self.tail_node
    if current_tail == None:
      self.tail_node = new_head

  # Add a new Node to the tail (end) of a doubly list
  # this is the same process as add_to_head, but for the tail
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    self.tail_node = new_tail
    if self.head_node == None:
      self.head_node = new_tail

  '''
  Due to the added tail property, removing the head of the list in a doubly linked list is a little more complicated than doing so in a singly linked list:

      Start by checking if there’s a current head to the list.
      If there isn’t, the list is empty, so there’s nothing to remove and the
      Preview: Docs Loading link description
      method
      ends
      Otherwise, update the list’s head to be the current head’s next node
      If the updated head is not None (meaning the list had more than one element when we started):
      Set the head’s previous node to None since there should be no node before the head of the list
      If the removed head was also the tail of the list (meaning there was only one element in the list):
      Call .remove_tail() to make the necessary changes to the tail of the list (we will create this method in the next exercise!)
      Finally, return the removed head’s value
  '''
  def remove_head(self):
    # Get the head_node ready for removal
    removed_head = self.head_node
    # If there is no head, nothing to do. End.
    if removed_head == None:
      return None
    # Set the new head node as the next_node of the current head
    self.head_node = removed_head.get_next_node()
    # if this is the head, remove the prev_node value as the head doesn't have a previous node
    if self.head_node != None:
      self.head_node.set_prev_node(None)
    # if this is the tail, it shouldn't have any nodes after it.
    if removed_head == self.tail_node:
      self.remove_tail()
    # return the value of the removed head (pop)
    return removed_head.get_value()
  
  ## Removing the tail is a mirror of removing head, like add_tail to add_head
  def remove_tail(self):
    removed_tail = self.tail_node
    if removed_tail == None:
      return None
    self.tail_node = removed_tail.get_prev_node()
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
    if removed_tail == self.head_node:
      self.remove_head()
    return removed_tail.get_value()
  
  '''
  Removing by Value I
  13 min

  In addition to removing the head and the tail of the list, it would also be useful to be able to remove a specific element from anywhere in the list.

  Imagine that you have a list of errands to run. You don’t always do your errands in order, so when you finish doing your laundry and want to cross it off, that could be somewhere in the middle of the list. We are going to build a .remove_by_value()
  Preview: Docs Loading link description
  method
  that will allow you to cross off (remove) that errand no matter where it is in the list.

  In order to do this:

    Iterate through the list to find the matching node
    If there is no matching element in the list:
    Return None
    If there is a matching node, we will then check to see if it is the head or tail of the list:
    If so, call the corresponding .remove_head() or .remove_tail() method
    If not, that means the node was somewhere in the middle of the list. In that case:
    Remove it by resetting the pointers of its previous and next nodes
    Finally, return the node’s value property
'''

  def remove_by_value(self, value_to_remove):
    # Prepare a variable to hold the node to remove
    node_to_remove = None
    # Start at the begining
    current_node = self.head_node
    # iterate over each node using current_node.get_next_node() while current_node has a value
    while current_node != None:
      if current_node.get_value() == value_to_remove:
        # when we find the value to remove, set the node_to_remove value to it
        node_to_remove = current_node
        # and end the loop
        break
      current_node = current_node.get_next_node()
    # if we didn't find value_to_remove, return None
    if node_to_remove == None:
      return None
    '''Now that we’ve found the node that we want to remove from the list (or returned None if it didn’t exist), 
        it’s time to actually remove the node. This means resetting the pointers around the node.

        There are three cases here:

          The node was the head of the list, in which case we can just call .remove_head()
          The node was the tail of the list, in which case we can just call .remove_tail()
          The node was somewhere in the middle of the list, 
            in which case we will need to manually change the pointers for its previous and next nodes

      '''
    # Check if the node to remove is the current head node. If not, drop the head
    if node_to_remove == self.head_node:
      self.remove_head()
    # Check if the node to remove is the tail. If not, drop the tail
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    # if not, the node is somewhere in the middle. 
    # We'll need to trim its pointers from the prev and next nodes
    # This will leave the node orphaned for garbage cleanup
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      next_node.set_next_node(next_node)
    # return the value of the dropped node
    return node_to_remove
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
'''
You finished your DoublyLinkedList class! Now we’re going to use that class to model a subway line. A doubly linked list is a great data structure to use to model a subway, as both have a first and last element, and are comprised of nodes (or stops) with links to the elements before and after them.

We will add to and remove stops from our subway line, and print it out to see what we’ve done. The .stringify_list()
Preview: Docs Loading link description
method
is the same as the one from the LinkedList class and has been provided for you.
'''
# Create your subway line here:
subway = DoublyLinkedList()
# Add our first stops at the top
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
# Add new stop at the end
print(subway.stringify_list())
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
print(subway.stringify_list())
# First and last station are temp closed. Remove.
subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())
# A station in the middle is closed. Remove.
subway.remove_by_value("Times Square")
print(subway.stringify_list())

test_list = DoublyLinkedList()
test_list.add_to_head(9)
test_list.remove_tail()
test_list.add_to_tail(8)
test_list.add_to_tail(2)
test_list.remove_head()
test_list.add_to_tail(4)
test_list.remove_by_value(9)
test_list.remove_head()
print(test_list.stringify_list())