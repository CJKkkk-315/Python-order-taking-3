import random
import matplotlib.pyplot as plt
x = []
yn = []
yp1 = []
yp2 = []
for i in range(1000):
    r = 5
    l = 5
    while True:
        if random.randint(0,1) == 0:
            r -= 1
        else:
            l -= 1
        if r == -1:
            yn.append(l)
            yp1.append(sum(yn) / len(yn))
            yp2.append(len([i for i in yn if i>=3])/len(yn))
            break
        if l == -1:
            yn.append(r)
            yp1.append(sum(yn)/len(yn))
            yp2.append(len([i for i in yn if i >= 3]) / len(yn))
            break
print(yp1)
print(yp2)
plt.plot(range(1000),yp1)
plt.axhline(y=1.7, color='r', linestyle='-')
plt.ylim(0, 5)
plt.xlabel('Count of Simulation')
plt.ylabel('Approximated Mean')
plt.show()
plt.plot(range(1000),yp2)
plt.axhline(y=0.29, color='r', linestyle='-')
plt.ylim(0, 1)
plt.xlabel('Count of Simulation')
plt.ylabel('Approximated Mean')
plt.show()

