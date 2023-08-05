from enum import Enum

class AbstractEnum(tuple, Enum):
    @property
    def word(self):
        return self.value[ 0 ]

    @property
    def subphrase(self):
        return self.value[ 1 ]

    @property
    def phrase(self):
        return self.value[ 2 ]

