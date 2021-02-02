class Array:
    def __init__(self, size):
        self.size = size
        self.a = [-1 for _ in range(size)]

    def retrive(self, index):

        if (index > self.size - 1):
            print("out of range")

        elif (self.a[index] != -1):
            print(self.a[index])

        else:
            print("not exist")

    def store(self, index, value):

        if (index > self.size - 1):
            print("out of range")

        elif (self.a[index] == -1):
            self.a[index] = value

        else:
            print("already exist. try another index")

    def show(self):
        print(self.a)


arr = Array(10)
arr.show()  # >>>[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
arr.store(0, 2)
arr.store(1, 4)
arr.show()  # >>>[2, 4, -1, -1, -1, -1, -1, -1, -1, -1]
arr.retrive(3)  # >>>not exist
arr.retrive(1)  # >>> 4
arr.store(1, 43)  # >>>already exist. try another index
arr.store(-5, 43)
arr.retrive(32)  # >>>out of range
arr.store(6, 23)  # >>>[2, 4, -1, -1, -1, 43, 23, -1, -1, -1]
arr.show()

"""
  class 배열 만들기
  a = [array_structure.Array(4) for i in range(3)]
  a[0].store(1, 3)
  a[1].store(1, 2)
  for i in range(3): a[i].show()

  >>>
  [-1, 3, -1, -1]
  [-1, 2, -1, -1]
  [-1, -1, -1, -1]
  """
