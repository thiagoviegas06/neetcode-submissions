class Solution:
    def isValid(self, s: str) -> bool:
        our_stack = Stack()
        for par in s:
            if par == "(" or par == "[" or par == "{":
                our_stack.push(par)
            else:
                if our_stack.isEmpty():
                    return False
                last_open = our_stack.pop()
                if par == ")":
                    if last_open != "(":
                        return False
                elif par == "]":
                    if last_open != "[":
                        return False
                else:
                    if last_open != "{":
                        return False
        return our_stack.isEmpty()
                    


class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = 0

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, new_item):
        self.stack.insert(self.pointer, new_item)
        self.pointer += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty, can't pop"

        self.pointer -= 1
        return self.stack.pop(self.pointer)
        