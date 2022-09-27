import sys
input = sys.stdin.readline

class Stack:
    def __init__(self) -> None:
        self.size = -1 
        self.top = -1
        self.stack = []

    def push(self, num):
        self.size += 1
        self.top += 1
        self.stack.append(num)

    def pop(self):
        if self.size == -1:
            print("-1")
        else:
            print(self.stack[self.top])
            del self.stack[self.top]
            self.top -= 1
            self.size -= 1 

    def size(self):
        print(self.size+1)

    def empty(self):
        if self.size== -1:
            print('1')
        else:
            print('0')

    def topp(self):
        if self.size == -1:
            print("-1")
        else:
            print(self.stack[self.top])

stack = Stack()

n = int(input())

command = input().split()

print(command)
for cmd in command:
    if "push" in cmd:
        cmd = cmd.strip("push ")
        stack.push(cmd)
    elif cmd == "pop":
        stack.pop()
    elif cmd == "size":
        stack.size()
    elif cmd == "empty":
        stack.empty()
    elif cmd == "top":
        stack.topp()