
a_list = [1,2,3]
print sum(a_list)

import random
def roll_dice(numbers = 3, points = None):
    print '<<<< ROLE THE DICE! >>>>'
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11<= total<= 18
    isSmall = 3<= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


    
    

    
def start_game():
    print '<<<< GAME STARTS! >>>>'
    choices = ['Big', 'Small']
    your_choice = input('Big or Small :')
    #your_choice = 'Small'
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)

        if youWin:
            print 'The points are', points, 'You win!'     
        else:
            print 'The points are', points, 'You Lose!'            
    else:
        print 'Invalid Words'
        start_game()

#start_game()


print '#------------------#'


 
def start_game_bet():
    account = 0
    while account >= 0:
        print '<<<< GAME STARTS! >>>>'
        choices = ['Big', 'Small']
        your_choice = input('Big or Small :')
        win_lose = input('How much you want bet ?')
                    
    #your_choice = 'Small'
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)

            if youWin:
                print 'The points are', points, 'You win!'
                account = account + win_lose
                print 'you gained ' + str(win_lose) + ', you have ' + str(account) +' now!'
            else:
                print 'The points are', points, 'You Lose!'
                account = account - win_lose
                print 'you lost ' + str(win_lose) + ', you have ' + str(account) +' now!'
        else:
            print 'Invalid Words'
            start_game()
        if account <=0:
            break
    print 'Game Over'
        
    
#start_game_bet()

print'#-------------------'

def if_CN_mobile(number):
    CN_mobile = ['134','135','136','137','138','139','150','151','152','157','158','159','182','183','184','187','188','147','178','1705']
    pre_number = number[:3]
    pre_number4 = number[:4]
    if pre_number in CN_mobile:
        operator = 'China Mobile'
        return operator
    if pre_number4 in CN_mobile:
        operator = 'China Mobile'
        return operator

def if_CN_union(number):
    CN_union = ['130','131','132','155','156','185','186','145','176','1709']
    pre_number = number[:3]
    pre_number4 = number[:4]
    if pre_number in CN_union:
        operator = 'China Union'
        return operator
    elif pre_number4 in CN_union:
        operator = 'China Union'
        return operator

def if_CN_telecom(number):
    CN_telecom = ['133','153','180','181','189','177','1700']
    pre_number = number[:3]
    pre_number4 = number[:4]
    if pre_number in CN_telecom:
        operator = 'China Telecom'
        return operator
    elif pre_number4 in CN_telecom:
        operator = 'China Telecom'
        return operator

def number_verify():
    number = input('Enter Your number :')
    str_number = str(number)
    num_length = len(str_number)
    if num_length == 11:
        mobile = if_CN_mobile(str_number)
        union = if_CN_union(str_number)
        telecom = if_CN_telecom(str_number)
        if mobile == 'China Mobile':
            print 'Operator: China Mobile'
            print 'We\'re sending verification code via text to your phone ' + str(number)
        elif union == 'China Union':
            print 'Operator: China Union'
            print 'We\'re sending verification code via text to your phone ' + str(number)
        elif telecom == 'China Telecom':
            print 'Operator: China Telecom'
            print 'We\'re sending verification code via text to your phone ' + str(number)
        else:
            print 'No such a operator'
        if bool(mobile) + bool(union) + bool(telecom) > 0:
            print 'Process finished with exit code 0'
        

    else:
        print ' Invalid length, your number should be in 11 digits'
        number_verify()
        
number_verify()


