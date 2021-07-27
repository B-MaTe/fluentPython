from collections import deque

dq = deque(range(10), maxlen=10)
# dq = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3) # Takes items and prepends them to the right, if n > 0, otherwise to the left
dq.appendleft(44) # Appends n, if reached maxlen, removes the other end
dq.extend([11,22,33]) # Adding items to the right, removes the same amount of items from the left
dq.extendleft([10,20,30,40]) # Same, but adds them to the left side, and reverses them:
# deque([40, 30, 20, 10, 9, 0, 1, 2, 3, 4], maxlen=10)


