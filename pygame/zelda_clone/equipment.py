from settings import WEAPON_DATA


class Equipment:

    def __init__(self, equipments):
        self.equipments = list(equipments.keys())
        self.index = 0

    @property
    def equiped(self):
        return self.equipments[self.index]

    def next(self):
        self.index = (self.index + 1) % len(self.equipments)


if __name__ == '__main__':
    weapon = Equipment(WEAPON_DATA)
    for i in range(5):
        weapon.next()
        print(weapon.equiped())
