
class CustomBaseException(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class IncorrectSexError(CustomBaseException):
    def __init__(self, identifier):
        super().__init__(f"Sex should either be male or female. In {identifier}")


class WrongDinoTypeError(CustomBaseException):
    def __init__(self, expresion, expected):
        super().__init__(f'Expected {expected} type, got {expresion} ')