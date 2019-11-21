from typing import List
from exceptions import IncorrectSexError, WrongDinoTypeError


class Dino:
    # TODO type should be class containers class <(Rex)>.
    def __init__(self,
                 name: str,
                 level: int,
                 sex: str,
                 dino_type: str,
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
            raise IncorrectSexError(identifier=name)

        self.name = name.lower()
        self.level = level
        self.sex = sex
        self.dino_type = dino_type

        self.health = health
        self.stamina = stamina
        self.oxygen = oxygen
        self.food = food
        self.weight = weight
        self.damage = damage
        self.movement_speed = ms
        self.torpidity = torp
        self.imprinting = impr

    def __hash__(self):
        return hash((self.name, self.sex, self.level, self.dino_type))

    def __eq__(self, other):
        if isinstance(other, Dino):
            return hash(self) == hash(other)


class DinoGroup:
    def __init__(self, name, dinos: List[Dino], dino_type=None):
        self._dinos = dinos
        self.name = name
        self.dino_type = dino_type

    @property
    def dinos(self):
        return self._dinos

    def get_dino_by_attribute(self, attr, attr_value):
        for dino in self._dinos:
            if getattr(dino, attr) == attr_value:
                return dino

    def __len__(self):
        return len(self.dinos)

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} composed mainly by: {self.dino_type}'


class DinoGroupMonoType(DinoGroup):

    def __init__(self, name, dinos, dino_type):
        super().__init__(name, dinos, dino_type=dino_type)
        self.group_type = self.dinos[0].dino_type  # First dino of the group decides the group type
        self._assert_dinotype()

    def _assert_dinotype(self):
        for dino in self.dinos:
            if dino.dino_type != self.group_type:
                raise WrongDinoTypeError(expected=self.group_type, expresion=dino.dino_type)