a = [25,26,24,29,4,7,9,12,2,18,16,5]
class Control:
    def max(self,a):
        return max(a)
    def min(self,a):
        return min(a)
    def avg(self,a):
        return sum(a)/len(a)
    def sort(self,a):
        return sorted(a,reverse=True)
    def append(self,a,b):
        a.append(b)
c = Control()
print(c.max(a))
print(c.min(a))
print(c.avg(a))
print(c.sort(a))
c.append(a,20)
print(a.index(29))
print(a[3])
