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
        # stack이 array의 기존 사이즈만큼 꽉 찼을 경우 array 크기 2배로 조정
        if self.isFull():
            tmp = [0 for _ in range(self.capacity)]
            self.array += tmp
            self.capacity *= 2

        self.top += 1
        self.array[self.top] = value

    # stack에서 top이 가리키고 있는 값 뽑아냄
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            self.top -= 1
            return self.array[self.top + 1]

    # stack에서 top이 가리키고 있는 값 출력, pop과는 다름
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
s.showStack()  # >>> 2
s.push(3)
s.showStack()  # >>> 2 3
s.push(2)
s.showStack()  # >>> 2 3 2
s.push(3)
s.showStack()  # >>> 2 3 2 3
s.push(2)
s.showStack()  # >>> 2 3 2 3 2
s.push(3)
s.showStack()  # >>> 2 3 2 3 2 3
s.pop()
s.showStack()  # >>> 2 3 2 3 2
print("stack의 맨 위에 있는 값 : ", s.peek())  # >>> stack의 맨 위에 있는 값 : 2
s.pop()
s.showStack()  # >>> 2 3 2 3
print("stack의 맨 위에 있는 값 : ", s.peek())  # >>> stack의 맨 위에 있는 값 : 3
