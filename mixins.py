class CritMixin:
    def crit_attack(self, target):
        print(f"Критическая атака по {target.name}!")
        target.hp -= 2 * 10


class LoggerMixin:
    def log(self, message):
        print(message)

class SilenceMixin:
    def silence(self, target):
        print(f"{target.name} обезмолвлен (не может использовать навыки)!")
