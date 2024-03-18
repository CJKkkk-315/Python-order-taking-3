class Jx:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def zhouchang(self):
        return (self.a+self.b)*2
    def mianji(self):
        return self.a * self.b
a = float(input('请输入长:'))
b = float(input('请输入宽:'))
jx = Jx(a,b)
print('周长为:',jx.zhouchang())
print('面积为:',jx.mianji())