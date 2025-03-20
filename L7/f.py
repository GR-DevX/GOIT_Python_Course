from collections import deque

queue=deque()
print(f"Created:{queue}")
queue.append('a')
queue.append('t')
queue.append('b')
print(f'Filled:{list(queue)}')
queue.appendleft('b1')
queue.appendleft('b2')
print(f'Filled:{list(queue)}')
print(queue.pop())
print(f'Filled:{list(queue)}')
print(queue.popleft())
print(f'Filled:{list(queue)}')

#Deque
# pop appendleft - черга
# popleft append - теж черга, але в інший бік
# pop append - стек
# popleft appendleft - теж стек, але лівий))
# pop при порожній черзі - IndexError