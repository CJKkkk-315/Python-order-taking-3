
class Veterinarian:
    from collections import deque
    items = deque()
    def accept(self, petName):
        self.items.append(petName)
    def heal(self):
        if not self.items:
            raise IndexError('No pet are in the queue.')
        item = self.items.popleft()
        return item
if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian. heal())

