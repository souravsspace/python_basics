from enum import Enum


class Salery(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


# print(Salery.LOW)
# print(Salery.HIGH.value)
# print(Salery(2))
# print(Salery(2).value)
# print(Salery(2).name)
# print(Salery["LOW"])
# print(Salery["LOW"].value)
print(list(Salery))
print(len(Salery))
