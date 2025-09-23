from core import Warrior, Mage, Healer
from boss import Boss, AggressiveStrategy, DefensiveStrategy
from battle import Battle
from logger import RoundLogger


def main():
    warrior = Warrior("Аргус", strength=25, agility=15)
    mage = Mage("Лиан", intellect=30, agility=12)
    healer = Healer("Тея", intellect=20, agility=10)
    boss = Boss("Злобный Босс", strength=40, agility=10)

    team = [warrior, mage, healer]

    battle = Battle(team, boss)

    with RoundLogger():
        battle.fight()


if __name__ == "__main__":
    main()

