## Intro
Stacks provide three methods for interaction:
Push - add data to the "top" of the stack
Pop - return and remove data from the top of the stack
Peek - return data w/out removal from top of the stack

Gun clip
Stacked weights on barbell
Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. Each weight added becomes the new top of the stack.

At any point, the only weight you can remove, or pop, from the stack is the top one. You can peek and read the top weight without removing it from the stack.

The last plate that you put down becomes the first, and only, one that you can access. This is a Last In, First Out or LIFO structure. A less frequently used term is First In, Last Out, or FILO.

## Implementation

Stacks can be implemented using a linked list as the underlying data structure because it’s more efficient than a list or array. 

Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure will take up when it is “full.”

Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.

Review

Let’s take a minute to review what we’ve covered about stacks in this lesson.

Stacks:

    Contain data nodes
    Support three main operations
        Push adds data to the top of the stack
        Pop removes and provides data from the top of the stack
        Peek reveals data on the top of the stack
    Implementations include a linked list or array
    Can have a limited size
    Pushing data onto a full stack results in a stack overflow
    Stacks process data Last In, First Out (LIFO)
