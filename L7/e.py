from collections import deque

queue=deque()
print(f"Created:{queue}")
queue.append('a')
queue.append('t')
queue.append('b')
print(f'Filled:{list(queue)}')
print(f'Top: {queue[0]}')

print(f'Stealin element \'{queue.popleft()}\'')
print(f'Filled:{list(queue)}')
print(f'Top: {queue[0]}')
print(f'Is it empty? {len(queue)==0}')
print(f'Length: {len(queue)}')