from abc import ABC, abstractmethod


class BoundedStat:
    """Дескриптор для атрибутов с ограничениями."""

    def __init__(self, name, min_value=0, max_value=1000):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        if instance is None:
            return self  # возвращаем сам дескриптор при обращении через класс
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < self.min_value:
            value = self.min_value
        elif value > self.max_value:
            value = self.max_value
        instance.__dict__[self.name] = value


class Human:
    hp = BoundedStat("hp", 0, 1000)
    mp = BoundedStat("mp", 0, 1000)
    strength = BoundedStat("strength", 1, 100)
    agility = BoundedStat("agility", 1, 100)
    intellect = BoundedStat("intellect", 1, 100)

    def __init__(self, name, level=1, hp=100, mp=50, strength=10, agility=10, intellect=10):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.agility = agility
        self.intellect = intellect

    @property
    def is_alive(self):
        return self.hp > 0


class Character(Human, ABC):
    @abstractmethod
    def basic_attack(self, target):
        pass

    @abstractmethod
    def use_skill(self, target):
        pass

import random

class Warrior(Character):
    def basic_attack(self, target):
        damage = random.randint(self.strength, self.strength * 2)
        print(f"{self.name} наносит базовый удар {target.name} на {damage} урона")
        target.hp -= damage

    def use_skill(self, target):
        damage = random.randint(self.strength * 2, self.strength * 3)
        print(f"{self.name} использует мощный удар воина на {damage} урона по {target.name}")
        target.hp -= damage


class Mage(Character):
    def basic_attack(self, target):
        damage = random.randint(self.intellect, self.intellect * 2)
        print(f"{self.name} колдует базовое заклинание, нанося {damage} урона {target.name}")
        target.hp -= damage
        self.mp -= 5

    def use_skill(self, target):
        damage = random.randint(self.intellect * 3, self.intellect * 4)
        print(f"{self.name} использует мощное заклинание на {damage} урона по {target.name}")
        target.hp -= damage
        self.mp -= 20


class Healer(Character):
    def basic_attack(self, target):
        damage = random.randint(self.intellect // 2, self.intellect)
        print(f"{self.name} наносит слабый удар {target.name} на {damage} урона")
        target.hp -= damage

    def use_skill(self, team):
        possible_targets = [c for c in team if c.is_alive]
        if not possible_targets:
            print(f"{self.name} не может лечить, все игроки мертвы")
            return

        target = random.choice(possible_targets)
        heal = random.randint(self.intellect * 2, self.intellect * 4)
        print(f"{self.name} лечит {target.name} на {heal} здоровья")
        target.hp = min(target.hp + heal, target.__class__.hp.max_value)
        self.mp -= 15

# core.py
from mixins import CritMixin, LoggerMixin, SilenceMixin
import random

class Warrior(Character, CritMixin, LoggerMixin):
    def basic_attack(self, target):
        if random.random() < 0.3:  # 30% шанс крита
            self.crit_attack(target)
            self.log(f"{self.name} провёл критический удар по {target.name}")
        else:
            damage = random.randint(self.strength, self.strength * 2)
            print(f"{self.name} атакует {target.name} на {damage} урона")
            target.hp -= damage

    def use_skill(self, target):
        damage = random.randint(self.strength * 2, self.strength * 3)
        print(f"{self.name} использует мощный удар воина на {damage} урона по {target.name}")
        target.hp -= damage

class Mage(Character, SilenceMixin, LoggerMixin):
    def use_skill(self, target):
        if random.random() < 0.2:  # 20% шанс заглушить Босса
            self.silence(target)
            self.log(f"{self.name} заглушает {target.name}")
        damage = random.randint(self.intellect * 3, self.intellect * 4)
        print(f"{self.name} использует заклинание по {target.name} ({damage} урона)")
        target.hp -= damage
        self.mp -= 20

    def basic_attack(self, target):
        damage = random.randint(self.intellect, self.intellect * 2)
        print(f"{self.name} колдует базовое заклинание, нанося {damage} урона {target.name}")
        target.hp -= damage
        self.mp -= 5

class Healer(Character, LoggerMixin):
    def use_skill(self, team):
        possible_targets = [c for c in team if c.is_alive]
        if not possible_targets:
            self.log(f"{self.name} не может лечить")
            return
        target = random.choice(possible_targets)
        heal = random.randint(self.intellect * 2, self.intellect * 4)
        print(f"{self.name} лечит {target.name} на {heal} здоровья")
        target.hp = min(target.hp + heal, target.__class__.hp.max_value)
        self.mp -= 15

    def basic_attack(self, target):
        damage = random.randint(self.intellect // 2, self.intellect)
        print(f"{self.name} наносит слабый удар {target.name} на {damage} урона")
        target.hp -= damage