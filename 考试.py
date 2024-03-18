# 1
L1=[1,3,5,6]
L2=[2,4,5,8]
for i in L2:
    if i in L1:
        L1.remove(i)

# 2
n = int(input())
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
print(f(n))
# 3

# 4
import random
n = int(input())
s = []
for i in range(n):
    a = random.randint(1,1000)
    if a not in s:
        s.append(a)
s.sort()
print(s)

# 5
try:
    n = float(input())
    n = n**2
    with open('output.txt','w') as f:
        f.write(str(n))
except:
    print('输入数值有误')
# 6
d = {}
with open('/tmp/data.txt','r') as f:
    data = f.readlines()
for i in data:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i,j in d.items():
    if j > 200:
        print(i.replace('\n',''),'出现',str(j),'次')
# 7
class Animal(object):
    time = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('animal can eat')
# 8
class Dog(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, age)
        self.color = color
    def eat(self):
        Animal.eat()
    def feed(self):
        self.time += 1
# 9
import threading
a_event = threading.Event()
b_event = threading.Event()
def print_a(event, next_event):
    for i in range(10):
        event.wait()
        print('a')
        event.clear()
        next_event.set()
def print_b(event, next_event):
    for i in range(10):
        event.wait()
        print('b')
        event.clear()
        next_event.set()
a_thread = threading.Thread(target=print_a, args=(a_event, b_event))
b_thread = threading.Thread(target=print_b, args=(b_event, a_event))
a_thread.start()
b_thread.start()
a_event.set()
