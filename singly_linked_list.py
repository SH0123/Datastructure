class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.first = None
        self.size = 0

    def isEmpty(self):
        return self.first == None

    def append(self, node):
        self.size += 1
        # 1)비어있는 리스트에 추가
        if self.isEmpty():
            node.next = self.first
            self.first = node
        # 2)리스트 맨 뒤에 추가
        else:
            curn = self.first
            while curn:
                if curn.next == None:
                    break
                curn = curn.next
            node.next = curn.next
            curn.next = node

    # return node
    def findNode(self, index):
        idx = 0
        curn = self.first
        while idx < index:
            if curn:
                prev = curn
                curn = curn.next
                idx += 1
            else:
                break

        if curn == None:
            return None

        return curn, prev

    # return node
    def findPreviousNode(self, index):
        if self.findNode(index) == None:
            return None

        return self.findNode(index)[1]

    # return index
    def findIndex(self, data):
        idx = 0
        curn = self.first
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1

        return None

    # findNode 함수 사용
    def insertIndex(self, index, node):
        pass

    # findIndex 함수 사용
    def insertData(self, data, node):
        pass

    # findPreviousNode, findNode 함수 사용
    def deleteData(self, index):
        pass

    def showList(self):
        curn = self.first
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)

    def deleteList(self):
        self.first = None


s = SinglyLinkedList()
s.append(Node(1))
s.append(Node(24))
s.append(Node(32))
s.showList()
print(s.findNode(4)[0])
print(s.findPreviousNode(2).data)
print(s.findIndex(34)[1])
s.deleteList()
s.showList()
