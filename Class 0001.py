# -*- coding: utf-8 -*-
#All the Cokes are the same and all the Coke are good. Liz Taylor > knows it, the President konws it, the bum knows it, and you know > it. -- Andy Warhol

class CocaCola():
    it_taste = 'So good!'
coke_for_bum = CocaCola()
coke_for_president = CocaCola()
print coke_for_bum.it_taste
print coke_for_president.it_taste

#Class Atrribute
class CocaCola:
    formula = ['caffeine','sugar','water','soda']


coke_for_me = CocaCola()
coke_for_you = CocaCola()
print CocaCola.formula
#print CocaCola.it_taste --- Wrong
print coke_for_me.formula
print coke_for_you.formula

for element in coke_for_you.formula:
    print element

class CocaCola():
    formula = ['caffeine','sugar','water','soda']
coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐' # Instance Atrribute
for element in coke_for_China.formula:
    print element
    print coke_for_China.local_logo

#print CocaCola.local_logo


class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print('Energy!')

coke = CocaCola()
coke.drink()

print '#---------------'
class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def drink(coke):
        print 'Energy!'

coke = CocaCola()
print bool(coke.drink() == CocaCola.drink(coke))
coke.drink()
CocaCola.drink(coke)


class CocaCola:
    formula = ['caffine','sugar','water','soda']
    def drink(self,how_much):

        if how_much == 'a sip':
            print 'Cool~'
        elif how_much == 'whole bottle':
            print 'Headache!'
ice_coke = CocaCola()
ice_coke.drink('a sip')

print '#------------------'


class CocaCola:
    formula = ['caffine','sugar','water','soda']
    def _init_(self):
        self.local_logo = '可口可乐'

    def drink(self):
        print 'Energy'

coke = CocaCola()
print coke.local_logo

