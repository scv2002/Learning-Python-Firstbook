

password_list = ['*#*#', '12345']

def account_login():
    tries =3
    while tries > 0:
        password = input ('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print 'Login success!'
            break
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print 'Password has changed successfuly!'
            account_login()
        else:
            print 'Wrong password or invalid input!'
            tries = tries - 1
            print tries, 'time left'
    else:
        print 'Your account has been suspended'

# account_login()

def text_create(file_name):
    desktop_path = 'C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/'
    file_path = desktop_path + str(file_name) + '.txt'
    file = open(file_path,'w')
    file.write((str(file_name) + '*')*3)
    file.close()
    print file_path

times = 10
#while times > 0:
#    text_create(times)
#    times = times - 1


print ' # --------------- '

def invest(account, rate, time):
    payback = account * ((1.0 + rate)**time)
    return payback
def invest_1(account, rate, time):
    payback = account * (1.0 + rate*time)
    return payback

time_1 = 1
while time_1 <= 8:
    payback = invest(100, 0.05, time_1)
    print 'year' + str(time_1) + ' :  $ ' + str(payback)
    payback_1 = invest_1(100, 0.05, time_1)
    print 'year' + str(time_1) + ' :  $ ' + str(payback_1)
    difference = payback - payback_1
    print 'year' + str(time_1) + ' difference :  $' + str(difference)
    time_1 = time_1 + 1



print ' # --------------- '

odd = 0
odd_string = [odd]
for odd in range (1,101):
    if odd%2 == 0:
         file = open('C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/odd.txt','r+')
         file.write(str(odd) + '\n')
         file.close()
         
         #odd_string = odd_string.append(odd)
         print odd

print ' # --------------- '



    
         
     
            
