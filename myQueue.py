class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            else:
                while len(self.stack1) != 0:
                    ele = self.stack1.pop()
                    self.stack2.append(ele)
        return  self.stack2[len(self.stack2) - 1]

    def pop(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            else:
                while len(self.stack1) != 0:
                    ele = self.stack1.pop()
                    self.stack2.append(ele)
        return self.stack2.pop()


queue = MyQueue()
queue.push(1)
print(queue.pop())
queue.push(2)
queue.push(3)
print(queue.top())
print(queue.pop())

