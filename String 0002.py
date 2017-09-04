#coding: utf-8

search = '168'
num_a= '1386-168-0006'
num_b= '1681-222-0006'

print search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a'
print search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b'


print '{} a word she can get what she {} for.'.format('with', 'came')

print '{preposition} a word she can gete what she {verb} for'.format(preposition = 'With', verb = 'came')

print '{0} a word she can get what she {1} for.'.format('With,', 'came')


city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print url

