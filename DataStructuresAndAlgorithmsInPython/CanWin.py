#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    '제비 뽑기'라는 게임을 제작하려고 한다.
    규칙은 다음과 같다.
        - 유저는 임의의 제비 N개를 선택한다. 
        - 각 제비에는 자연수가 적혀있다.
        - 제비들을 숫자가 보이지 않게 뒤집는다.
        - 그 후, 임의로 제비 한 장을 골라 숫자를 확인하고 다시 덮어두는 과정을 4번 반복했을 때, 확인된 4개의 숫자의 합이 K가 될 수 있는 확률이 존재한다면 승리한다.
        - 동일한 숫자를 뽑을 수도 있다.
        - 예를 들어 N=5, K=12일 때, 유저가 선택한 제비가 아래와 같다면,
            1, 3, 6, 2, 9
        - 차례로 6,2,2,2가 적힌 제비를 확인할 경우 합이 12가 되고, 유저는 승리한다.
    [문제]
    당신은 유저가 선택한 제비의 목록과 K가 주어졌을 때, 유저가 승리할 수 있는지 판단하는 함수를 만들어야 한다.
    아래의 지시사항을 확인하여 함수를 구현해보자.

    [제한사항]
        - N <= 10
        - K <= 40

    [함수 정의]
        // input: 뽑은 제비가 담긴 배열 numbers, 만들고자 하는 값 K
        // return: 승리할 수 있는지 여부 T/F
        boolean canWin(int[] numbers, int k)
'''

'''
    s: 지금까지 더한 수
    m: 더할 수 있는 남은 횟수
    k: 찾는 합계
'''
def find(numbers, s, m, k):
    if m is 1:
        i = 0
        while i < len(numbers):
            print "sum: " + str(s + numbers[i])
            if s + numbers[i] is k:
                return True
            elif s + numbers[i] > k:
                return False
            i = i + 1
        return False
    else:
        i = 0
        while i < len(numbers):
            if s + numbers[i] > k:
                return False
            else:
                result = find(numbers, s + numbers[i], m-1, k)
                if result is True:
                    return True
                i = i + 1


def canWin(numbers, k):
    if len(numbers) > 10 or k > 40:
        return False

    i = 0
    s = 0
    m = 4
    result = False
    while i < len(numbers):
        s = numbers[i]
        result = find(numbers, s, m-1, k)
        if result is True:
            return result
        i = i + 1
    return result

assert(canWin([1,3,6,2,9],12) == True)
assert(canWin([1,3,6,2,9],39) == False)