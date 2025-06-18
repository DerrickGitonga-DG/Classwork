"""
A stack is a data structure that follows the LIFO principle - Last In, First Out.
Think of a stack like a stack of plates: you put plates on top (push), and you take plates from the top (pop).
You can only access the top plate, not the ones below.
"""

# Using Python List as Stack
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)  # Expected: [10, 20, 30]

# Peek
top_element = stack[-1]
print("Top element is:", top_element)  # Expected: 30

# Check if empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")  # Expected here

# Using Custom Class
class SimpleStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("STACK IS EMPTY")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top:", self.items)

# Main
if __name__ == "__main__":
    stack1 = SimpleStack()
    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    stack1.print_stack()
    print("Top element:", stack1.peek())
    print("Popped:", stack1.pop())
    stack1.print_stack()
    print("Is stack empty?", stack1.is_empty())
    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping all?", stack1.is_empty())