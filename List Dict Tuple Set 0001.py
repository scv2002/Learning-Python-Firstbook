

# list = [val1,val2,val3,val4]
# dict = {key1:val1,key2:val2,key3:vale}
# tuple = (vala1,val2,val3,val4)
# set = {val1,val2,val3,val4}

Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']
print Weekday[0]

all_in_list = [1,   #整数
               1.0,   #浮点数
               'a word'   #字符串
               #print '1'   #函数
               #True,   #布尔值
               #[1,2],   #列表中套列表
               #(1,2),   #元组
               #{'key':'value'}   #字典
               ]
print all_in_list

fruit = ['pineapple',
         'pear'
         ]
fruit.insert(2,'grape')
print fruit

fruit[0:0] = ['Orange']
print fruit

fruit.remove('grape')
print fruit

fruit[0] = 'Grapefruit'
print fruit

del fruit[0:2]
print fruit

periodic_table = ['H',
                  'He',
                  'Li',
                  'Be',
                  'B',
                  'C',
                  'N',
                  'O',
                  'F',
                  'Ne'
                  ]
print periodic_table[0]
print periodic_table[-2]
print periodic_table[0:3]
print periodic_table[-10:-7]
print periodic_table[-10:]
print periodic_table
print periodic_table[:9]

string_string = 'string'
print string_string[2]


NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
    }
print NASDAQ_code

key_test = {'None void': 'a Test'}
print key_test

a = {'key':123,'key':1234}
print a

NASDAQ_code['EN'] = 'Energizer'
print NASDAQ_code


NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print NASDAQ_code

del NASDAQ_code['FB']
print NASDAQ_code
                
print NASDAQ_code['TSLA']

#chart[1:4] # WRONG!

letters = ('a','b','c','d','e','f','g')
print letters[1]

a_set = {1,2,3,4}
print a_set
a_set.add(5)
print a_set
a_set.discard(5)
print a_set

num_list = [6.2,7.4,1,3,5]
print sorted(num_list)
print num_list

