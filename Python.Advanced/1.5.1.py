class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        self.capacity -= v


x = MoneyBox(10)

print(x.capacity)
print(x.can_add(34), x.can_add(10), x.can_add(9))
x.add(7)

print(x.capacity)
print(x.can_add(2), x.can_add(10))
