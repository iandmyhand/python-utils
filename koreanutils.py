##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Korean.
If you want to test this util, run in the terminal below code.
    $ python3 koreanutils.py
"""
import unittest

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015 SeomGi, Han, Python Utils Project'

__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Development'


class TestKoreanUtils(unittest.TestCase):

    def test_is_valid_korean_ssn(self):
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('1234561234567'))


class KoreanUtils:

    def is_valid_korean_ssn(self, ssn):
        """
        usage:
            KoreanUtils().is_valid_korean_ssn('1234561234567') returns false
        refernece:
            https://github.com/kenu/egov/blob/master/ok.commoncomp/src/main/java/egovframework/com/utl/fcc/service/EgovNumberCheckUtil.java
        """

        # 입력값이 숫자인지 확인
        if not ssn.isdigit():
            return False

        # 주민등록번호 자리수 확인
        if 13 != len(ssn):
            return False

        id_add = "234567892345"  # 주민등록번호에 가산할 값
        count_num = 0
        add_num = 0
        total_id = 0  # 검증을 위한 변수선언

        for index in range(len(ssn)):
            print(str(index))

        return True


if __name__ == '__main__':
    unittest.main()
