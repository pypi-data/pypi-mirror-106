import math
import random

from typing import Set


class ConfirmationCode:
    @property
    def length(self):
        return self.__length

    @property
    def symbols(self):
        return self.__symbols

    @property
    def default_symbol_set(self) -> set:
        return set(str(s) for s in range(0, 10))

    def __init__(self, length: int = 4, symbols: Set[str] = None):
        if symbols is None:
            symbols = self.default_symbol_set

        self.__length = length
        self.__symbols = list(symbols)

    def mirror(self) -> str:
        need_insert_reversed_first_symbol = self.__get_half_length() % 2

        symbols = self.random(self.__get_half_length())

        return symbols + symbols[::-1][need_insert_reversed_first_symbol:]

    def half_and_random(self) -> str:
        repeated_symbols = ''.join(self.random(1) * self.__get_half_length())
        random_symbols = self.random(self.__length - self.__get_half_length())

        symbols = [repeated_symbols]
        symbols.extend(random_symbols)

        random.shuffle(symbols)

        return ''.join(symbols)

    def sequence(self, length: int = None) -> str:
        if length is None:
            length = self.__length

        sorted_symbols = sorted(self.symbols)

        if length > len(sorted_symbols):
            multiplier = math.ceil(length / len(sorted_symbols))
            sorted_symbols *= multiplier

        start_position = random.randint(0, len(sorted_symbols) - length)
        reverse = random.choice([-1, 1])

        sequence = sorted_symbols[start_position:start_position + length][::reverse]

        return ''.join(sequence)

    def two_sequence(self) -> str:
        first_sequence = self.sequence(self.__get_half_length())
        second_sequence = self.sequence(self.__length - self.__get_half_length())

        sequences = [first_sequence, second_sequence]
        random.shuffle(sequences)

        return ''.join(sequences)

    def simplest(self) -> str:
        return ''.join(self.random(1) * self.__length)

    def random(self, length: int = None) -> str:
        if length is None:
            length = self.__length

        return ''.join(random.choices(k=length, population=self.__symbols))

    def __get_half_length(self):
        return math.ceil(self.__length / 2)
