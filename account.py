# This Python file uses the following encoding: Windows-1251
from my_menu import menu
import os
import json
import datetime # Импортируем библиотеку для работы с датой 
account_menu_puncts='- пополнить счет;- совершить покупку;- история покупок;- выход'.split(';')
his=[]
def check():
    value=load_value('account.txt')
    print ('на счете', value, 'рублей')
    his=load_hist('account.json')
    while True:
        choise=menu(account_menu_puncts)
        if choise==1:
            v=get_value('Введите вносимую сумму\n')
            value=put(value,v)
            print ('на счете', value, 'рублей')
            
        if choise==2:
            name=input('Введите название товара\n')
            price=get_value('Введите стоимость товара\n')
            value=shop(value,price,name)
        if choise==3:
            hist()
        if choise==4:
            save_value('account.txt',value)
            save_hist('account.json')
            break

def put(value,v):
    if  value>=0:  
        value+=v
    
    return value
def shop(value,price,name):
    if  price>=0:  # Как же жалко исправлять эту ошибку. Потратил отрицательную сумму и шопься сколько влезет.
        if value>price:
            value-=price
            purchase={'date':str(datetime.date.today()),
                'name':name,
                'price':price}
            his.append(purchase)
            
            print ('на счете', value, 'рублей')
        else:
            print('Дорого')
    return value
def hist():
    print(his)

def save_value(path,value):
    with open(path, 'wt') as f:
        f.write(str(value))
def load_value(path):
    if os.path.exists(path)==False:
        return 0
    with open(path, 'rt') as f:
        return int(f.read())
def save_hist(path):
    with open(path, 'w') as f:
       # for purshcase in his:
            json.dump(his, f)
def load_hist(path):
    his=[]
    if os.path.exists(path)==False:
        return his
    with open(path, 'r') as f:
        his=json.load(f)
    return his

