#math_game 0.1
from random import randrange
def oson(a1,b1):
    cfunk = randrange(1,5)
    if a1>b1:
        if cfunk == 1:
            funk = '+'
            c=a1+b1
        elif cfunk == 2:
            funk = '-'
            c=a1-b1
        elif cfunk == 3:
            funk = '*'
            c=a1*b1
        else:
            if a1%b1==0:
                funk = '/'
                c=a1/b1
            else:
                funk = '-'
                c=a1-b1
        print(f'{a1} {funk} {b1} = ')
        a = input('Answer: ')

        if a.isdigit() == True:
            a = int(a)    
            if a == c:
               print("Good")
            else:
                print('Wrong')
        
        else:
            print('Error. Exit Ctrl+C ')
while True:
    daraja = input('Choise you level (easy/normal/hard): ')
    if daraja == 'easy':
        while True:
            a1 = randrange(1,10)
            b1 = randrange(1,10)
            if a1>b1:
                oson(a1,b1)
    elif daraja == 'normal':
        while True:
            a1 = randrange(1,20)
            b1 = randrange(1,20)
            if a1>b1:
                oson(a1,b1)
    elif daraja == 'hard':
        while True:
            a1 = randrange(2,30)
            b1 = randrange(2,30)
            if a1>b1:
                oson(a1,b1)
    else:
        print('Level error!')
