# This Python file uses the following encoding: Windows-1251
from my_menu import menu
import os
import json
import datetime # ����������� ���������� ��� ������ � ����� 
account_menu_puncts='- ��������� ����;- ��������� �������;- ������� �������;- �����'.split(';')
his=[]
def check():
    value=load_value('account.txt')
    print ('�� �����', value, '������')
    his=load_hist('account.json')
    while True:
        choise=menu(account_menu_puncts)
        if choise==1:
            v=int(input('������� �������� �����\n'))
            value=put(value,v)
            print ('�� �����', value, '������')
            
        if choise==2:
            name=input('������� �������� ������\n')
            price=int(input('������� ��������� ������\n'))
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
    if  price>=0:  # ��� �� ����� ���������� ��� ������. �������� ������������� ����� � ������ ������� ������.
        if value>price:
            value-=price
            purchase={'date':str(datetime.date.today()),
                'name':name,
                'price':price}
            his.append(purchase)
            
            print ('�� �����', value, '������')
        else:
            print('������')
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