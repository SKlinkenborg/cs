# Queues: Conceptual

## Intro
Queue is a data structure containing an ordered set of data
Provide 3 methods of interaction:
    * Enqueue - adds data to the "back" / end of the queue
    * Dequeue - provide and removes the data from the "front" or beginning of queue
    * Peek - Reveal data from "from" of queue w/out removing it

Examples: a line of people retrieving movie tickets they bought online. Each person has a name (data). First item is front and back of queue. New people get added to the back of the queue.
The next person's name is checked (peeked) then after getting a ticket they're removed from the line (dequeued).

Queues are FIFO First In First Out

## Implementation
Can be implemented as a linked list for underlying data structure.
But limited subset of rules since can only interact with front and back.
Since front and back must be accessible, values must be maintained.

A Bounded Queue has limitations on length.
Attemptimg to queue data beyond the bound results in a Queue Overflow.
Attempting to dequeue from an empy queue results in Queue Underflow.

# Summary
* Contain data nodes
* Support three main operations:
* Enqueue adds data to the back of the queue
* Dequeue removes and provides data from the front of the queue
* Peek provides data on the front of the queue
* Can be implemented using a linked list or array
* Bounded queues have a limited size.
* Enqueueing onto a full queue causes a queue overflow
* Queues process data First In, First Out (FIFO)
