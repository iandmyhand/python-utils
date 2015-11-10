##-*- coding: utf-8 -*- 
#!/usr/bin/python
'''
Number to Hangul string util.
'''

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015, Python Utils Project'

__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Production'


HANGUL_NUMBER = [
    '', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십'
]
HANGUL_NUMBER_UNIT = [
    '', '십', '백', '천'
]
HANGUL_NUMBER_BIG_UNIT = [
    '', '만', '억', '조', '경', '해'
]


class NumberUtils:

    def __init__(self):
        pass

    def convert_number_to_hangul_string(self, number_value):
        result = ''
        string_value = str(number_value)
        len_string_value = len(string_value)
        if string_value and string_value.isdigit():
            index = 0
            while index < len_string_value:
                single_result = ''
                hangul_number = HANGUL_NUMBER[int(string_value[index])]
                if hangul_number:
                    unitindex = ((len_string_value - index) % 4) - 1
                    single_result += hangul_number + HANGUL_NUMBER_UNIT[unitindex]
                if (len_string_value - index - 1) % 4 == 0:
                    big_unitindex = (len(string_value) - index - 1) // 4
                    if len(HANGUL_NUMBER_BIG_UNIT) > big_unitindex:
                        single_result += HANGUL_NUMBER_BIG_UNIT[big_unitindex]
                result += single_result
                index += 1

        return result
