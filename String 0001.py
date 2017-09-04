#coding: utf-8


print 'Hello World!'

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print artist_intro

num = 1
string = '1'

print int(string) + num

word = 'string'
print type(word)

words = 'word' * 8
print words

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) -num ) #等价于字符串'bang!'*4
print total

name = 'MyName is Mike'
print name[0]
print name[-4]
print name[11:14] # from 11th to 14th, 14th one is excluded.
print name[11:15]
print name[5:]
print name[:5]

#找出你朋友中的魔鬼
word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print find_the_evil_in_your_friends

url = 'http://wwl.site.cn/14d2e8ejwlexjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print file_name

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*'*9)
print(hiding_number)



