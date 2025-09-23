class Item:
    def __init__(self, name, effect=None):
        self.name = name
        self.effect = effect

    def use(self, target):
        print(f"{target.name} использует предмет {self.name}")
        if self.effect:
            self.effect.apply(target)


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def use_item(self, index, target):
        if 0 <= index < len(self.items):
            self.items[index].use(target)

