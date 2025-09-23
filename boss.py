from abc import ABC, abstractmethod
from core import Character

class Strategy(ABC):
    @abstractmethod
    def execute(self, boss, targets):
        pass


class AggressiveStrategy(Strategy):
    def execute(self, boss, targets):
        target = max(targets, key=lambda c: c.hp)
        damage = boss.strength * 3
        print(f"{boss.name} агрессивно атакует {target.name} на {damage} урона")
        target.hp -= damage


class DefensiveStrategy(Strategy):
    def execute(self, boss, targets):
        boss.hp += boss.strength * 2
        print(f"{boss.name} защищается, восстанавливая здоровье. HP={boss.hp}")


class Boss(Character):
    def __init__(self, name, level=20, hp=550, mp=100, strength=30, agility=15, intellect=20):
        super().__init__(name, level, hp, mp, strength, agility, intellect)
        self.strategy = AggressiveStrategy()

    def change_strategy(self, strategy):
        self.strategy = strategy

    def basic_attack(self, target):
        damage = self.strength * 2
        print(f"{self.name} наносит базовый удар {target.name} на {damage} урона")
        target.hp -= damage

    def use_skill(self, targets):
        self.strategy.execute(self, targets)
