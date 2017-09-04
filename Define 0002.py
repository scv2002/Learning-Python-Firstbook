# Python practice

def g_kg_converter(g):
    g2kg = str(g/1000 + 0.0) + 'kg'
    return g2kg

print g_kg_converter(35000)
print 'test#1'


def get_third_side_len(a, b):
    third_len_square = pow(a, 2) + pow(b, 2)
    extracting_n = 0.5
    print float(extracting_n)
    third_len = '''The right triangle third side's length is {}'''.format( pow (third_len_square, extracting_n))
    return third_len
third_len_R = get_third_side_len(4, 3)
print third_len_R
print 'test#2'

print float(3/2)
# Do you konw how to devide the number well?

def trapezoid_area(base_up, base_down, height):
    return 0.5*(base_up + base_down) * height
trapezoid_1 = trapezoid_area(1,2,3)
print trapezoid_1
print 'test#3'

print trapezoid_area(height=3, base_down=2, base_up=1) # Right
# print trapezoid_area(height=3, base_down=2, 1)  # Wrong
print trapezoid_area(base_up=1, base_down=2, height = 3) # Right
print trapezoid_area(1, 2, height=3) # Right
print 'test#4'

base_up = 1
base_down = 2
height = 3
print trapezoid_area(height, base_down, base_up)
print 'test#5'

print trapezoid_area(base_up=1, base_down=2, height = 4)
print height
print 'test#6'

print trapezoid_area(height=2, base_down=2, base_up=1)
print height
print 'test#7'

trapezoid_area(1,2,8)
print '   *', '  *','***' '  |'

print 'first line, \n second line'

print '   * \n  ***\n******\n   |'
print 'test#8'

def trapezoid_area(base_up, base_down, height = 3):
    return 0.5*(base_up + base_down)*height
print trapezoid_area(1,2)
print trapezoid_area(1,2, height = 15)
print trapezoid_area(1,2)
print 'test#9'
# EXAMPLE
# request.get(url, headers=header)
# img.save(img_new, img_format, quality=100)

file = open('C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/Text.txt','w')
file.write('Hello World!!')
file.close()
print 'test#10'
def text_create(name, msg):
    desktop_path = 'C:/Users/Songf/Desktop/Cases/121 Practice/Python practice/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done.')
text_create('hello', 'helloworld!!!')
print text_create('hello', 'hello_world!!!')
print 'test#11'

def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
text_filter('Python is lame!')
print text_filter( 'Python is lame!')

def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
    print clean_msg

censored_text_create('Try', 'Lame!lame!lame!')
print 'test#12'
print censored_text_create('Try', 'Lame!lame!lame!')
print 'test#13'

print 3**8
print 3/2 + (3%2)
print 3/2
print 3%2
print 3//2
