# This Python file uses the following encoding: Windows-1251
from my_menu import menu
account_menu_puncts='- ��������� ����;- ��������� �������;- ������� �������;- �����'.split(';')
value=0
his={}
def check():
    value=0
    print ('�� �����', value, '������')
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
    v=int(input('������� �������� �����'))
    value+=v
    print ('�� �����', value, '������')
def shop():
    global value
    price=int(input('������� ��������� ������'))
    if value>price:
        name=input('������� �������� ������')
        value-=price
        his[name]=price
        print ('�� �����', value, '������')
    else:
        print('������')

def hist():
    print(his)

