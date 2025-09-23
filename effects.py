class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def apply(self, target):
        print(f"Применяется эффект {self.name} к {target.name}")


class Buff(Effect):
    def apply(self, target):
        target.strength += 5
        print(f"{target.name} получает бафф силы +5")


class Debuff(Effect):
    def apply(self, target):
        target.strength -= 5
        print(f"{target.name} получает дебафф силы -5")

class SilenceEffect(Effect):
    def apply(self, target):
        print(f"{target.name} обезмолвлен (не может использовать навыки)!")
