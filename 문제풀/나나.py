import sys
from collections import deque
input = sys.stdin.readline
 
N = int(input())
buttons = deque()
 
for _ in range(N):
    info = list(input().split())
    if buttons and info[0] == "3":
        buttons.pop()
    else:
        buttons.append(info)
 
words = deque()
for button in buttons:
    if button[0] == "1":
        words.append(button[1])
    elif button[0] == "2":
        words.appendleft(button[1])
 
result = 0
if words:
    result = "".join(words)
print(result)