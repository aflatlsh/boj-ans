from collections import deque
import sys
input = sys.stdin.readline

deq = deque()

for i in range(int(input())):
    cmd = input().strip()
    if 'push' in cmd:
        deq.append(int(cmd.split()[1]))
    if cmd == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    if cmd == 'size':
        print(len(deq))
    if cmd == 'empty':
        print(1 if len(deq) == 0 else 0)
    if cmd == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            val = deq.popleft()
            deq.appendleft(val)
            print(val)
    if cmd == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            val = deq.pop()
            deq.append(val)
            print(val)
