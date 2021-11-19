import random
def MyDickSize():
    l=['8','=','D']
    for size in range(random.randint(0,101)):
        l.insert(2 , '=')
    print('your dick size is: ')
    for i in l:
        print(i, end='')
    print()

while True:
    input('press enter to reveal dick size')
    MyDickSize()


