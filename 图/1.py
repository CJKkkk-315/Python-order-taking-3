class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None
class LinkList():
    def __init__(self):
        self.head = None
    def create(self, item):
        self.head = Node(item[0])
        p = self.head
        for i in item[1:]:
            p.next = Node(i)
            p = p.next
    def print(self):
        p = self.head
        while p != None:
            print(p.item, end=' ')
            p = p.next
        print('')
    def getItem(self, index):
        p = self.head
        count = 0
        while count != index:
            p = p.next
            count += 1
        return p.item
    def setItem(self, index, item):
        p = self.head
        count = -1
        while count < index - 1:
            p = p.next
            count += 1
        p.item = item
    def swapItem(self, i, j):
        t = self.getItem(j)
        self.setItem(j, self.getItem(i))
        self.setItem(i, t)
    def quicksortofloop(self, left, right):
        if left < right:
            i = left
            j = i + 1
            start = self.getItem(i)
            while (j <= right):
                while (j <= right and self.getItem(j) >= start):
                        j += 1
                if (j <= right):
                    i += 1
                    self.swapItem(i, j)
                    j += 1
            self.swapItem(left, i)
            self.quicksortofloop(left, i - 1)
            self.quicksortofloop(i + 1, right)

linklist = []
f = ['红心','黑桃','方片','梅花']
for i in range(4):
    for j in range(1,14):
        linklist.append([f[i],j])
L = LinkList()
L.create(linklist)
print('排序前：')
L.print()
L.quicksortofloop(0, 51)
print('排序后：')
L.print()
import random
people = [[], [], [], []]
for i in range(4):
    for j in range(13):
        while True:
            p = random.randint(0,51)
            item = L.getItem(p)
            if item not in people[0] and item not in people[1] and item not in people[2] and item not in people[3]:
                people[i].append(item)
                break
for i in range(len(people)):
    print(str(i+1)+'号玩家的牌',people[i])
