# -*- coding: utf-8 -*-

import string
print string.punctuation

class CocaCola():
    fomula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self):
        self.local_logo = '可口可乐'
    def drink(self):
        print 'Energy'
coke = CocaCola()
print coke.local_logo

print '#---------------'

class CocaCola():
    fomula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self):

        for element in self.fomula:
            print'Coke has {}!'.format(element)
            
    def drink(self):
        print 'Energy!'

coke = CocaCola()
print coke.fomula
print coke.drink()

print '#----------------'

class CocaCola():
    fomula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print 'Energy!'

coke = CocaCola('可口可乐')
print coke.local_logo

print '#-----------------'

class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructorse Corn syrup',
        'Carbonated Water',
        'Natural Flavors',
        'Caramel color',
        'Caffeine'
        ]

    def __init__ (self, logo_name):
        self.local_logo = logo_name
    def drink(self):
        print 'you got {} cal energy!'.format(self.calories)

#类的继承 inheritanace 覆盖 override

class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural flavors',
        'Caramel Color',
        ]

coke_a = CaffeineFree('CocaCola Caffeine-Free')
coke_a.drink()
print coke_a.local_logo
print coke_a.ingredients
print coke_a.caffeine

        
print '#-----------------'
class TestA:
    attr = 1
obj_a = TestA()
TestA.attr = 42
print obj_a.attr

print TestA.attr
obj_b = TestA()
print obj_b.attr


print '#------------'
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42

print obj_a.attr
print obj_b.attr

class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
print obj_a.attr

print '#--------------'

print TestA.__dict__
print obj_a.__dict__

print '#---------------'

obj1 = 1
obj2 = 'String'
obj3 = []
obj4 = {}
obj5 = ()
print type(obj1),type(obj2),type(obj3),type(obj4),type(obj5)

from Beautifulsoup import BS4
soup = BeautifulSoup
print type(soup)





