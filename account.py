# This Python file uses the following encoding: Windows-1251
from my_menu import menu
account_menu_puncts='- ��������� ����;- ��������� �������;- ������� �������;- �����'.split(';')
his={}
def check():
    value=100
    print ('�� �����', value, '������')
    while True:
        choise=menu(account_menu_puncts)
        if choise==1:
            v=int(input('������� �������� �����'))
            print ('�� �����', put(value,v), '������')
            
        if choise==2:
            name=input('������� �������� ������')
            price=int(input('������� ��������� ������'))
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
    if  price>=0:  # ��� �� ����� ���������� ��� ������. �������� ������������� ����� � ������ ������� ������.
        if value>price:
            value-=price
            his[name]=price
            print ('�� �����', value, '������')
        else:
            print('������')
    return value
def hist():
    print(his)

