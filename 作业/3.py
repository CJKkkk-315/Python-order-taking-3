class Computer:
    def __init__(self,band,color,size):
        self.band = band
        self.color = color
        self.size = size


band = input('品牌：')
color = input('颜色：')
size = input('内存大小：')
computer = Computer(band,color,size)
print(computer.band)
print(computer.color)
print(computer.size)