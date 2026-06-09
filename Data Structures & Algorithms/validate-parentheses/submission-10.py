class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()

        if len(s) % 2 != 0 or len(s) == 0:
            return False

        for ch in s:
            if ch in "{[(":
                stack.push(ch)

            elif ch == '}':
                out = stack.pop()
                if out != '{':
                    return False

            elif ch == ']':
                out = stack.pop()
                if out != '[':
                    return False

            elif ch == ')':
                out = stack.pop()
                if out != '(':
                    return False

        return stack.size() == 0