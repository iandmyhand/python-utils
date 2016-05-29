##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Korean.
If you want to test this util, run in the terminal below code.
    $ python3 koreanutils.py
"""
import re
import unittest

from dateutils import DateUtils


class TestKoreanUtils(unittest.TestCase):

    def test_is_valid_korean_ssn(self):
        instance = KoreanUtils()
        self.assertFalse(instance.is_valid_korean_ssn(None))
        self.assertFalse(instance.is_valid_korean_ssn('1234567890123'))
        self.assertFalse(instance.is_valid_korean_ssn('2001011111111'))
        self.assertFalse(instance.is_valid_korean_ssn('9012310000000'))
        self.assertFalse(instance.is_valid_korean_ssn('5000001234567'))

        # self.assertTrue(instance.is_valid_korean_ssn(''))

    def test_is_valid_foreign_ssn(self):
        instance = KoreanUtils()
        self.assertFalse(instance.is_valid_foreign_ssn(None))
        self.assertFalse(instance.is_valid_foreign_ssn('1234567890123'))
        self.assertFalse(instance.is_valid_foreign_ssn('2001011111111'))
        self.assertFalse(instance.is_valid_foreign_ssn('9012310000000'))
        self.assertFalse(instance.is_valid_foreign_ssn('5000001234567'))

        # self.assertTrue(instance.is_valid_foreign_ssn(''))

    def test_is_valid_ssn(self):
        instance = KoreanUtils()
        self.assertFalse(instance.is_valid_foreign_ssn(None))
        self.assertFalse(instance.is_valid_foreign_ssn('1234567890123'))
        self.assertFalse(instance.is_valid_foreign_ssn('2001011111111'))
        self.assertFalse(instance.is_valid_foreign_ssn('9012310000000'))
        self.assertFalse(instance.is_valid_foreign_ssn('5000001234567'))

        # self.assertTrue(instance.is_valid_korean_ssn(''))
        # self.assertTrue(instance.is_valid_foreign_ssn(''))

    def test_is_building_number(self):
        instance = KoreanUtils()
        self.assertFalse(instance.is_building_number(None))
        self.assertTrue(instance.is_building_number('46-4'))
        self.assertFalse(instance.is_building_number('아리수로'))
        self.assertTrue(instance.is_building_number('975'))
        self.assertFalse(instance.is_building_number('천호대로'))

    def test_get_divide_to_road_address_and_building_number(self):
        instance = KoreanUtils()
        self.assertEqual(('', ''), instance.divide_to_road_address_and_building_number(None))
        self.assertEqual(('서울 강동구 아리수로', '46-4'), instance.divide_to_road_address_and_building_number('서울 강동구 아리수로 46-4'))
        self.assertEqual(('서울 강동구 천호대로', '975'), instance.divide_to_road_address_and_building_number('서울 강동구 천호대로 975'))
        self.assertEqual(('강원 강릉시 주문진읍 울릉3길', '1'), instance.divide_to_road_address_and_building_number('강원 강릉시 주문진읍 울릉3길 1'))
        self.assertEqual(('서울 구로구 시흥대로', '525 (태천대)'), instance.divide_to_road_address_and_building_number('서울 구로구 시흥대로 525 (태천대)'))


class KoreanUtils:

    def divide_to_road_address_and_building_number(self, full_road_address):
        if not full_road_address:
            return '', ''

        _road_address = full_road_address if full_road_address else ''
        _building_number = ''

        _full_road_address_arr = full_road_address.split(' ')
        for i in reversed(range(0, len(_full_road_address_arr))):
            if self.is_building_number(_full_road_address_arr[i]):
                _road_address = ' '.join(_full_road_address_arr[:i])
                _building_number = ' '.join(_full_road_address_arr[i:])
                break

        return _road_address, _building_number
    
    def is_building_number(self, building_number_string):
        if not building_number_string:
            return False
        _pattern = re.compile('[0-9]+([\-]+[0-9]+)*')
        if re.search(_pattern, building_number_string) is None:
            return False
        return True

    def is_valid_ssn(self, ssn):
        if not ssn:
            return False

        # 입력값이 숫자인지 확인
        if not ssn.isdigit():
            # print('ssn is not digit.')
            return False

        # 주민등록번호 자리수 확인
        if 13 != len(ssn):
            # print('Length of ssn is not equal to 13.')
            return False

        if int(ssn[6]) in [1, 2, 3, 4]:
            return self.is_valid_korean_ssn(ssn)
        elif int(ssn[6]) in [5, 6, 7, 8]:
            return self.is_valid_foreign_ssn(ssn)
        return False

    def is_valid_korean_ssn(self, ssn):
        """
        usage:
            KoreanUtils().is_valid_korean_ssn('1234561234567') returns False
        refernece:
            http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EB%B2%88%ED%98%B8%EC%9C%A0%ED%9A%A8%EC%84%B1%EC%B2%B4%ED%81%AC
            https://github.com/kenu/egov/blob/master/ok.commoncomp/src/main/java/egovframework/com/utl/fcc/service/EgovNumberCheckUtil.java
        """

        if not ssn:
            return False

        # 입력값이 숫자인지 확인
        if not ssn.isdigit():
            # print('ssn is not digit.')
            return False

        # 주민등록번호 자리수 확인
        if 13 != len(ssn):
            # print('Length of ssn is not equal to 13.')
            return False

        # 주민등록번호 앞자리 날짜 및 성별구분 숫자 유효성 체크
        if 0 == int(ssn[0]) or 1 == int(ssn[0]):
            if not int(ssn[6]) in [3, 4]:
                # print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '20' + str(ssn[0:6])
        else:
            if not int(ssn[6]) in [1, 2]:
                # print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '19' + str(ssn[0:6])

        if not DateUtils().is_valid_date(birthdate):
            # print('birthdate: ' + birthdate)
            return False

        id_add = '234567892345'  # 주민등록번호에 가산할 값
        total_id = 0  # 검증을 위한 변수

        for index in range(len(ssn) - 1):
            count_num = int(ssn[index])
            add_num = int(id_add[index])
            total_id += count_num * add_num

        # 마지막 유효숫자와 검증식을 통한 값 비교
        if (11 - (total_id % 11)) % 10 != int(ssn[12]):
            # print('total_id%11: ' + str(total_id % 11) + ' | 11-(total_id % 11))%10: ' + str((11 - (total_id % 11)) % 10) + ' | ssn[12]: ' + ssn[12])
            return False

        return True

    def is_valid_foreign_ssn(self, ssn):
        """
        usage:
            KoreanUtils().is_valid_foreign_ssn('1234561234567') returns False
        refernece:
            http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:%EB%B2%88%ED%98%B8%EC%9C%A0%ED%9A%A8%EC%84%B1%EC%B2%B4%ED%81%AC
            https://github.com/kenu/egov/blob/master/ok.commoncomp/src/main/java/egovframework/com/utl/fcc/service/EgovNumberCheckUtil.java
        """

        if not ssn:
            return False

        # 입력값이 숫자인지 확인
        if not ssn.isdigit():
            # print('ssn is not digit.')
            return False

        # 외국인등록번호 자리수 확인
        if 13 != len(ssn):
            # print('Length of ssn is not equal to 13.')
            return False

        # 외국인등록번호 앞자리 날짜 및 성별구분 숫자 유효성 체크
        if 0 == int(ssn[0]) or 1 == int(ssn[0]):
            if not int(ssn[6]) in [7, 8]:
                # print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '20' + str(ssn[0:6])
        else:
            if not int(ssn[6]) in [5, 6]:
                # print('ssn[0]:' + ssn[0] + '|ssn[6]:' + ssn[6])
                return False
            birthdate = '19' + str(ssn[0:6])

        if not DateUtils().is_valid_date(birthdate):
            # print('birthdate: ' + birthdate)
            return False

        # 외국인등록번호 검증식
        check = 0
        for i in range(len(ssn) - 1):
            check += ((9 - i % 8) * int(ssn[i]))

        if 0 == check % 11:
            check = 1
        elif 10 == check % 11:
            check = 0
        else:
            check = check % 11

        if 9 < check + 2:
            check = check + 2 - 10
        else:
            check = check + 2

        if int(ssn[12]) != check:
            return False

        return True


if __name__ == '__main__':
    unittest.main()
