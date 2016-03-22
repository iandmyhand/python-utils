import hangul

s = 'ㅎㅏㄴㅅㅓㅁㄱㅣ'
print(hangul.conjoin(s))

s = '한섬기'
print(hangul.conjoin(s))

print(ord('ㅎ'))
print(ord(u'\u1112'))
print(chr(12622))
print(chr(4370))
print(hex(12622))
print(hex(4370))
