# This Python file uses the following encoding: Windows-1251
from my_menu import menu
account_menu_puncts='- пополнить счет;- совершить покупку;- история покупок;- выход'.split(';')
his={}
def check():
    value=100
    print ('на счете', value, 'рублей')
    while True:
        choise=menu(account_menu_puncts)
        if choise==1:
            v=int(input('Введите вносимую сумму'))
            print ('на счете', put(value,v), 'рублей')
            
        if choise==2:
            name=input('Введите название товара')
            price=int(input('Введите стоимость товара'))
            shop(value,price,name)
        if choise==3:
            hist()
        if choise==4:
            break

def put(value,v):
    if  value>=0:  
        value+=v
    
    return value
def shop(value,price,name):
    if  price>=0:  # Как же жалко исправлять эту ошибку. Потратил отрицательную сумму и шопься сколько влезет.
        if value>price:
            value-=price
            his[name]=price
            print ('на счете', value, 'рублей')
        else:
            print('Дорого')
    return value
def hist():
    print(his)

