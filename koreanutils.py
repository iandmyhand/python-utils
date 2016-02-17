##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Korean.
If you want to test this util, run in the terminal below code.
    $ python3 koreanutils.py
"""
import unittest

from dateutils import DateUtils


class TestKoreanUtils(unittest.TestCase):

    def test_is_valid_korean_ssn(self):
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('1234567890123'))
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('2001011111111'))
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('9012310000000'))
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('5000001234567'))

        # self.assertTrue(KoreanUtils().is_valid_korean_ssn('...'))


class KoreanUtils:

    def is_valid_korean_ssn(self, ssn):
        """
        usage:
            KoreanUtils().is_valid_korean_ssn('1234561234567') returns false
        refernece:
            http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EB%B2%88%ED%98%B8%EC%9C%A0%ED%9A%A8%EC%84%B1%EC%B2%B4%ED%81%AC
            https://github.com/kenu/egov/blob/master/ok.commoncomp/src/main/java/egovframework/com/utl/fcc/service/EgovNumberCheckUtil.java
        """

        # 입력값이 숫자인지 확인
        if not ssn.isdigit():
            print('ssn is not digit.')
            return False

        # 주민등록번호 자리수 확인
        if 13 != len(ssn):
            print('Length of ssn is not equal to 13.')
            return False

        # 주민등록번호 앞자리 날짜 및 성별구분 숫자 유효성 체크
        if 0  == int(ssn[0]) or 1 == int(ssn[0]):
            if 4 < int(ssn[6]):
                print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '20' + str(ssn[0:6])
        else:
            if 2 < int(ssn[6]):
                print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '19' + str(ssn[0:6])

        if not DateUtils().is_valid_date(birthdate):
            print('birthdate: ' + birthdate)
            return False

        id_add = '234567892345'  # 주민등록번호에 가산할 값
        total_id = 0  # 검증을 위한 변수

        for index in range(len(ssn) - 1):
            count_num = int(ssn[index])
            add_num = int(id_add[index])
            total_id += count_num * add_num

        # 마지막 유효숫자와 검증식을 통한 값 비교
        if (11 - (total_id % 11)) % 10 != int(ssn[12]):
            print('total_id%11: ' + str(total_id % 11) + ' | 11-(total_id % 11))%10: ' + str((11 - (total_id % 11)) % 10) + ' | ssn[12]: ' + ssn[12])
            return False

        return True


if __name__ == '__main__':
    unittest.main()
