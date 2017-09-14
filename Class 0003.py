# coding: utf-8


# C:\Users\Songf\Desktop\Cases\121 Practice\Python practice
ln_path = 'C:/Users/Songf/Desktop/Cases/121 Practice/PyCharm project/last_name.txt'
fn_path = 'C:/Users/Songf/Desktop/Cases/121 Practice/PyCharm project/first_name.txt'
file = open(ln_path,'w')
file.write('Hello world, Again')
file.close()

file = open(fn_path,'w')
file.write('John Kitty, Ted Allen')
file.close()


fn = []
ln1 = []  # 单字名
ln2 = []  # 双字名
with open(fn_path, 'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])
print fn

with open(ln_path, 'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
print ln1
print '=' * 7  # 分割线
print ln2
print '天涯明月刀'


# 将打印结果拷贝入元组 fn = (), ln1 = (), ln2 = ()

# import random
# class FakeUser:
#    def fake_name(self, one_world=False, two_worlds=False):
#        if one_word:
#            full_name = random.choice(fn) + random.choice(ln1)
#        elif two_world:
#            full_name = random.choice(fn) + random.choice(ln1)
#        else:
#            full_name = random.choice(fn) + random.choice(ln1 + ln2)
#        print full_name

# class SnsUser(FakeUser):
#    def get_followers(self,few=True, a_lot=False):
#        if few:
#            followers = random.randrange(1,50)
#        elif a_lot:
#            followers = random.randrange(200,10000)
#    print(follwers)
# user_a = FakeUser()
# user_b = SnsUser()
# user_a.fake_name()
# user_b.get_follwers(few=True)
