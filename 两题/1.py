class MovingTotal:
    def __init__(self):
        self.numbers = []
        self.totals = set()
    def append(self, numbers):
        for i in numbers:
            self.numbers.append(i)
            if len(self.numbers) >= 3:
                self.totals.add(self.numbers[-1]+self.numbers[-2]+self.numbers[-3])
    def contains(self, total):
            return total in self.totals
if __name__ == "__main__":

    movingtotal =MovingTotal()
    movingtotal.append([1,2,3,4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    movingtotal.append([5,7])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    movingtotal1 = MovingTotal()
    print(movingtotal1.contains(12))
