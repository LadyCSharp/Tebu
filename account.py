# This Python file uses the following encoding: Windows-1251
from my_menu import menu
account_menu_puncts='- пополнить счет;- совершить покупку;- история покупок;- выход'.split(';')
value=0
his={}
def check():
    value=0
    print ('на счете', value, 'рублей')
    while True:
        choise=menu(account_menu_puncts)
        if choise==1:
            put()
        if choise==2:
            shop()
        if choise==3:
            hist()
        if choise==4:
            break

def put():
    global value
    v=int(input('Введите вносимую сумму'))
    value+=v
    print ('на счете', value, 'рублей')
def shop():
    global value
    price=int(input('Введите стоимость товара'))
    if value>price:
        name=input('Введите название товара')
        value-=price
        his[name]=price
        print ('на счете', value, 'рублей')
    else:
        print('Дорого')

def hist():
    print(his)

