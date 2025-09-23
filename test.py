# tests/test_core.py
from core import Warrior

def test_warrior_attack():
    w = Warrior("Тест", 100, 40)
    class DummyTarget:
        def __init__(self):
            self.name = "Враг"
            self.hp = type("stat", (), {"value": 50})()
    t = DummyTarget()
    w.basic_attack(t)
    assert t.hp.value == 40
