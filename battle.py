import random
from core import Character, Human
from boss import Boss
from core import Healer

class TurnOrder:
    def __init__(self, characters):
        self.characters = sorted(characters, key=lambda c: c.agility, reverse=True)

    def __iter__(self):
        return iter(self.characters)


class Battle:
    def __init__(self, team, boss):
        self.team = team
        self.boss = boss
        self.turn_order = TurnOrder(team + [boss])
        self.effects = []

    def apply_effects(self):
        for effect in self.effects[:]:
            effect.apply(self.boss)
            effect.duration -= 1
            if effect.duration <= 0:
                self.effects.remove(effect)

    def print_status(self):
        print(f"Статус после хода:")
        print(f"  Босс {self.boss.name}: HP = {self.boss.hp}")
        for member in self.team:
            print(f"  Игрок {member.name}: HP = {member.hp}")
        print("-" * 30)

    def fight(self):
        print("Начинается бой!")
        while self.boss.is_alive and any(c.is_alive for c in self.team):
            for character in self.turn_order:
                if not character.is_alive:
                    continue
                self.apply_effects()
                if character == self.boss:
                    character.use_skill(self.team)
                else:
                    if isinstance(character, Healer):
                        character.use_skill(self.team)
                    else:
                        if random.random() < 0.5:
                            character.basic_attack(self.boss)
                        else:
                            character.use_skill(self.boss)
                self.print_status()
                if not self.boss.is_alive:
                    print("Команда выиграла!")
                    return
                if not any(c.is_alive for c in self.team):
                    print("Босс выиграл!")
                    return


