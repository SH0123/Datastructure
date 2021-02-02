class Stack(object):
    def __init__(self, maxSize):
        self.array = [0 for _ in range(maxSize)]
        self.top = -1
        self.capacity = maxSize

    def isEmpty(self):
        return self.top < 0

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            tmp = [0 for _ in range(self.capacity)]
            self.array += tmp
            self.capacity *= 2

        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            self.top -= 1
            return self.array[self.top + 1]

    def peek(self):
        if self.isEmpty():
            return -1

        else:
            return self.array[self.top]

    def showStack(self):
        if self.isEmpty():
            return -1

        string = ""
        for idx in range(self.top + 1):
            string += str(self.array[idx]) + " "

        print(string)


s = Stack(5)
s.push(2)
s.showStack()
s.push(3)
s.showStack()
s.push(2)
s.showStack()
s.push(3)
s.showStack()
s.push(2)
s.showStack()
s.push(3)
s.showStack()
s.pop()
s.showStack()
print("stack의 맨 위에 있는 값 : ", s.peek())
s.pop()
s.showStack()
print("stack의 맨 위에 있는 값 : ", s.peek())
