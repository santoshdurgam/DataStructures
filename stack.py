class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def sprint(self):
        print(self.stack)
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.sprint()

print(st.peek())

st.pop()
st.sprint()