# Coding: UTF-8

def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32.0
    return str(fahrenheit) + 'F'

C2F = fahrenheit_converter(35)
print C2F

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)

print '粿'


def fahrenheit_converter_1(C):
    fahrenheit = C * 9/5 + 32.0
    print(str(fahrenheit)+ 'F')

C2F_1 = fahrenheit_converter_1(35)
print C2F_1
