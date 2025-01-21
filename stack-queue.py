from collections import deque

# Queue
queue = deque()

# Enqueue elements
queue.append("a")
queue.append("b")
queue.append("c")

# Dequeue elements
first_element = queue.popleft()

queue_size = len(queue)

# Stack
stack = deque()

# Push elements
stack.append("a")
stack.append("b")
stack.append("c")

# Pop elements
last_element = stack.pop()

stack_size = len(stack)
