from collections import deque
n = int(input())

queue = deque()
for i in range(n, 0, -1):
    queue.append(i)

while len(queue) > 1:
    queue.pop()
    queue.rotate()
print(*queue)