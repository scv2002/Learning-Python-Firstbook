# Build-in Data Structure

num_list = [6,2,7,4,1,3,5,6]
print (sorted(num_list))

print sorted(num_list, reverse= True)
print num_list

#num = 'number'
#str = 'string'
num = [3,5,7,9]
str = ['a','b','c','d','e']
for a,b in zip(num,str):
    print b, 'is', a
    
#数据结构 推导式 List comprehension

a = []
for i in range(1,11):
    a.append(i)
    print a    

b = [ i for i in range(1,11)]
print b

import time

a = []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print time.clock() - t0, 'seconds process time'

t0 = time.clock()
b = [i for i in range(1,2000)]
print time.clock() - t0, 'seconds process time'

a = [i**2 for i in range(1,10)]
print a
c = [ j+1 for j in range(1,10)]
print c
k = [n for n in range(1,10) if n % 2 == 0]
print k
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print z


letters = ['a','b','c','d','e','f','g']
for num,letter in enumerate(letters):
    print letter, ' is ',num + 1

print enumerate(letters)


lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
print words


#path = 'C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/Walden.txt'
#with open(path, 'r') as text:
#    words = text.read().split()
#    print words
#    for word in words:
#        print '{} - {} times'.format(word,words.count(word))

import string

#path = 'C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/Walden.txt'

#with open(path,'r') as text:
#    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
#    words_index = set(words)
#    counts_dict = {index:words.count(index) for index in words_index}

#for word in sorted(counts_dict, key = lambda x: counts_dict[x], reverse = True):
#    print '{} -- {} times'.format(word, counts_dict[word])

print string.punctuation

# Lambda 表达式
# key = lambda x: counts_dict[x]


                                  
