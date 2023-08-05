import math
import random
import hashlib

from typing import Set


class Code:
    @property
    def hash(self):
        """
        Return sha256 code hash
        :return:
        """
        return hashlib.sha256(self.__code.encode()).hexdigest()

    @property
    def code(self):
        """
        Return code
        :return:
        """
        return self.__code

    def __init__(self, code: str):
        """
        Code constructor
        :param code:
        """
        self.__code = code

    def __str__(self):
        """
        Return code as str
        :return:
        """
        return self.__code

class PrettyCode:
    """
    Some methods to generate easy-to-remember code.
    """

    @property
    def length(self):
        """
        Return code length
        :return:
        """
        return self.__length

    @property
    def symbols(self):
        """
        Return symbols set
        :return:
        """
        return self.__symbols

    @property
    def default_symbol_set(self) -> set:
        """
        Return string set contains number 0..9
        :return:
        """
        return {str(s) for s in range(0, 10)}

    def __init__(self, length: int = 4, symbols: Set[str] = None):
        """
        If symbols doesnt set using default symbol set {0..9}
        :param length:
        :param symbols:
        """
        if symbols is None:
            symbols = self.default_symbol_set

        self.__length = length
        self.__symbols = list(symbols)

    def mirror(self) -> Code:
        """
        Return string "XYZZYZ"
        :return:
        """
        need_insert_reversed_first_symbol = self.__length % 2

        symbols = self.random(self.__get_half_length()).code

        return Code(symbols + symbols[::-1][need_insert_reversed_first_symbol:])

    def half_and_random(self) -> Code:
        """
        Return string "XXXABC"
        :return:
        """
        repeated_symbols = ''.join(self.random(1).code * self.__get_half_length())
        random_symbols = self.random(self.__length - self.__get_half_length()).code

        symbols = [repeated_symbols]
        symbols.extend(random_symbols)

        random.shuffle(symbols)

        return Code(''.join(symbols))

    def sequence(self, length: int = None) -> Code:
        """
        Return string "ABCDEF"
        :param length:
        :return:
        """
        if length is None:
            length = self.__length

        sorted_symbols = sorted(self.symbols)

        if length > len(sorted_symbols):
            multiplier = math.ceil(length / len(sorted_symbols))
            sorted_symbols *= multiplier

        start_position = random.randint(0, len(sorted_symbols) - length)
        reverse = random.choice([-1, 1])

        sequence = sorted_symbols[start_position:start_position + length][::reverse]

        return Code(''.join(sequence))

    def two_sequence(self) -> Code:
        """
        Return string "ABCFED"
        :return:
        """
        first_sequence = self.sequence(self.__get_half_length()).code
        second_sequence = self.sequence(self.__length - self.__get_half_length()).code

        sequences = [first_sequence, second_sequence]
        random.shuffle(sequences)

        return Code(''.join(sequences))

    def simplest(self) -> Code:
        """
        Return string "YYYYYY"
        :return:
        """
        return Code(''.join(self.random(1).code * self.__length))

    def random(self, length: int = None) -> Code:
        """
        Return random string
        :param length:
        :return:
        """
        if length is None:
            length = self.__length

        return Code(''.join(random.choices(k=length, population=self.__symbols)))

    def __get_half_length(self) -> int:
        """
        Return half of current code length
        :return:
        """
        return math.ceil(self.__length / 2)
