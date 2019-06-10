from typing import List


class Dino:
    def __init__(self,
                 name: str,
                 identifier: str,
                 level: int,
                 sex: str,
                 health: int = None,
                 stamina: int = None,
                 oxygen: int = None,
                 food: int = None,
                 weight: int = None,
                 damage: int = None,
                 ms: int = None,
                 torp: int = None,
                 impr: int = None):

        if sex not in ('male', 'female'):
            print(f'Error: Sex can only be male or female on {self.id}')

        self.name = name
        self.id = identifier
        self.level = level

        self.health = health
        self.stamina = stamina
        self.oxygen = oxygen
        self.food = food
        self.weight = weight
        self.damage = damage
        self.movement_speed = ms
        self.torpidity = torp
        self.imprinting = impr


class DinoGroup:

    def __init__(self, dinos: List[Dino]):
        self._dinos = dinos

    @property
    def dinos(self):
        return self._dinos

    def __len__(self):
        return len(self.dinos)
