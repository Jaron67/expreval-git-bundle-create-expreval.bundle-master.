class Stack:
    """
    Array Implementation of a Stack Data Structure
    """
    def __init__(self):
        self.stack_array = []

    def __len__(self):
        return len(self.stack_array)

    def __bool__(self):
        return bool(self.stack_array)

    def clear(self):
        self.stack_array = []

    def push(self, item):
        self.stack_array.append(item)

    def pop(self):
        if self.stack_array:
            return self.stack_array.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if self.stack_array:
            return self.stack_array[-1]
        else:
            return None
