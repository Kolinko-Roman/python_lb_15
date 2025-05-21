# Завдання 1: Основний персонаж
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"{self.name} (рівень {self.level}) — Здоров'я: {self.health}, Атака: {self.attack}")

    def hit(self, other):
        other.health -= self.attack
        print(f"{self.name} атакує {other.name} на {self.attack} одиниць урону!")

    def heal(self):
        self.health += 10
        print(f"{self.name} відновлює 10 одиниць здоров'я!")

# Завдання 3: Класи Героїв
class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor

    def heal(self):
        self.health += 15
        print(f"{self.name} (воїн) відновлює 15 одиниць здоров'я!")

class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana

    def heal(self):
        if self.mana >= 10:
            self.health += 20
            self.mana -= 10
            print(f"{self.name} (маг) витрачає 10 мани та відновлює 20 здоров'я!")
        else:
            print(f"{self.name} (маг) не має достатньо мани для лікування.")

class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def heal(self):
        self.health += 10
        print(f"{self.name} (лучник) відновлює 10 одиниць здоров'я!")

# Завдання 2: Бій між персонажами
warrior = Warrior("Борис", 5, 100, 15, armor=10)
mage = Mage("Аліса", 4, 70, 20, mana=30)
archer = Archer("Ігор", 3, 80, 12, arrows=5)

warrior.info()
mage.info()
archer.info()

print("\n--- Початок бою ---\n")

warrior.hit(mage)
mage.hit(archer)
archer.hit(warrior)

print("\n--- Відновлення здоров'я ---\n")

warrior.heal()
mage.heal()
archer.heal()

print("\n--- Статус після бою ---\n")

warrior.info()
mage.info()
archer.info()
