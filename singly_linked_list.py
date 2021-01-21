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
        prev = None
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

    # findNode 함수 사용, 해당 index의 node 뒤에 insert
    def insertIndex(self, index, node):
        # 맨 앞에 node 추가하는 경우
        if index == -1:
            node.next = self.first
            self.first = node
        # 범위 초과하는 index 기입하는 경우
        elif self.findNode(index) != None:
            curnNode, _ = self.findNode(index)
            node.next = curnNode.next
            curnNode.next = node
        else:
            return -1

    # findIndex 함수 사용, 해당 data가 있는 node 뒤에 insert
    def insertData(self, data, node):
        # data를 포함하는 노드가 list에 존재하는 경우
        if self.findIndex(data) != None:
            idx = self.findIndex(data)
            self.insertIndex(idx, node)

        else:
            return -1

    # findPreviousNode, findNode 함수 사용
    def deleteIndex(self, index):
        if index == 0:
            curnNode, _ = self.findNode(index)
            self.first = curnNode.next
        elif self.findNode(index) != None:
            curnNode, prevNode = self.findNode(index)
            prevNode.next = curnNode.next
        else:
            return -1

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
s.append(Node(99))
s.showList()
s.insertIndex(2, Node(3))
s.showList()
s.insertData(24, Node(29))
s.showList()
s.deleteIndex(5)
s.showList()
s.deleteIndex(0)
s.showList()
s.insertIndex(-1, Node(130))
s.showList()
s.deleteList()
s.showList()
