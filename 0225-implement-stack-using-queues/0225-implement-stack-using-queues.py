class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)
        print(self.q1)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        top_element = self.q1.pop()
        self.q1 = self.q2
        self.q2 = []
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        top_element = self.q1[0]
        self.q2.append(top_element)
        self.q1 = self.q2
        self.q2 = []
        return top_element

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()