import random
from core import Character, Human
from boss import Boss
from core import Healer
import random
from effects import Buff, Debuff, Effect

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
        print(f"  Босс {self.boss.name}: HP = {self.boss.hp}", end="; Эффекты: ")
        print(", ".join([e.name for e in self.boss.active_effects]))
        for member in self.team:
            print(f"Игрок {member.name}: HP = {member.hp}; Эффекты: ", end="")
            if member.active_effects:
                print(", ".join([e.name for e in member.active_effects]))
            else:
                print("-")

    def fight(self):
        print("Начинается бой!")
        while self.boss.is_alive and any(c.is_alive for c in self.team):
            for character in self.turn_order:
                all_combatants = [self.boss] + self.team
                chosen = random.choice(all_combatants)
                effect_cls = random.choice([Buff, Debuff])
                effect = effect_cls(
                    name=effect_cls.__name__,
                    duration=random.randint(1, 3)
                )
                chosen.add_effect(effect)
                print(f"Случайный эффект {effect.name} добавлен к {chosen.name} на {effect.duration} раундов!")
                if not character.is_alive:
                    continue
                character.apply_effects()
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


