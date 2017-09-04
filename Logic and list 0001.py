
album = ['Black Star', 'David Bowie', 25, True]

album.append('new song')
album
print album

print album[0],album[3],album[-3]

print 33 in album
print '33 in album'
print "33 in album"
#print ''33 in album''
print '''33 in album'''
print '"33 in album"'

the_Eddie = 'Eddie'
name = 'Eddie'
print the_Eddie == name
print the_Eddie is name

print '# -----------'
print bool(0)
print bool(1)
print bool([])
print bool(False)
print bool(None)

print '# -----------'
a_thing = None
print a_thing
print bool(a_thing)

print '# -----------'
def account_login():
    password = input('Password:')
    password_correct = password == '12_345'
    if password_correct:
        print 'Login success!'
    else:
        print 'Wrong password or invalid input!'
        account_login()

# account_login()

print '# -----------'

password_list = ['*#*#','12345']
def account_login_1():
    password = input('Passowrd:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')

        password_list.append(new_password)
        print('Your password has changed successfully!')

        account_login_1()
    else:
        print('Wrong password or invalid input!')
        account_login_1()

# account_login_1()

print '# -----------'

# every_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for every_letter in 'Hello world':
    print every_letter
  
print '# -----------'

for num in range(1,11):
    print str(num) + '+ 1 =', num + 1

print '# -----------'


songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print song, ' - Dio'
    elif song == 'Thunderstruck':
        print song, ' - AC/DC'
    elif song == 'Rebel Rebel':
        print song, ' - David Bowie'

print song

        
print '# -----------'


#for i in range(1,10):
#    for j in range(1,10):
#        print str(i) + ' X ' + str(j)  + ' = ' + str(i*j)
#        print '{} X {} = {}'.format(i,j,i*j)

print '# -----------'

count = 0
while True:
    print 'Repeat this line !'
    count = count + 1
    if count == 5:
        break

print '# -----------'


    




    
            

