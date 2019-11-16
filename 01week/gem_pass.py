# -*- coding: UTF-8 -*-
import sys, random


class Gen_pass:

    def __init__(self):


        self._col_low_letter = 0
        self._col_up_letter = 0
        self._col_numeral = 0
        self._col_special_chr = 0
        self._total_symbol_psw = 0
        self._pass = []

    def set_type_letters(self, col_low_letter=10, col_up_letter=2, col_numeral=2, col_special_chr=2):
        self._col_low_letter = col_low_letter
        self._col_up_letter = col_up_letter
        self._col_numeral = col_numeral
        self._col_special_chr = col_special_chr

        MIN_COL_SYMBOLS_PSW = 8
        MAX_COL_SYMBOLS_PSW = 26

        self._total_symbol_psw = self._col_low_letter + self._col_up_letter + self._col_numeral + self._col_special_chr
        if self._total_symbol_psw < MIN_COL_SYMBOLS_PSW or self._total_symbol_psw > MAX_COL_SYMBOLS_PSW:
            print('Количество символов в пароле должно быть от 8 до 26.')
            return False

        return True

    def generation(self):

        list_up_letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

        list_low_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

        list_numeral = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        list_special_chr = ('!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-',
                            '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
                            '_', '{', '|', '}', '~')

        i = 0
        while i < self._col_low_letter:
            self._pass.append(list_low_letter[random.randint(0, len(list_low_letter) - 1)])
            i += 1

        i = 0
        while i < self._col_up_letter:
            self._pass.append(list_up_letter[random.randint(0, len(list_up_letter) - 1)])
            i += 1

        i = 0
        while i < self._col_numeral:
            self._pass.append(list_numeral[random.randint(0, len(list_numeral) - 1)])
            i += 1

        i = 0
        while i < self._col_special_chr:
            self._pass.append(list_special_chr[random.randint(0, len(list_special_chr) - 1)])
            i += 1

        random.shuffle(self._pass)


def main(args):
    gen_pass = Gen_pass()
    gen_pass.set_type_letters(8, 0, 2, 0)
    gen_pass.generation()
    print(''.join(gen_pass._pass))


if __name__ == "__main__":
    main(sys.argv)
