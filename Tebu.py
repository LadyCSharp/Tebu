# This Python file uses the following encoding: Windows-1251

from my_menu import *
from two_pic import some_pic
from victo import victorina,victorina1
#from account import check
import account
if __name__ == '__main__':
    
    menu_puncts='- ������� �����;- ������� (����/�����);- ���������� (����/�����);- �������� ����������� ������� ����������;- ���������� ������ �����;- ���������� ������ �����;- �������� ���������� �� ������������ �������;- ��������� ���������;- ������ � ���������;- ��� ���������� ����;- ����� ������� ����������;- �����.;- ������ ���� ����� ������ ��� �������� � ��������;- �������� ����������� ������� ����������'.split(';')
    pic_path=r'G:\Disk D\!!!lab\students\pictures'
    while True:
        choise=menu(menu_puncts)
        if choise==1:
            new_fold(input('������� ��� �����'))
        if choise==2:
            del_fold(input('������� ���'))    
        if choise==3:
            my_copy(input('������� ���'))
        if choise==4: 
            dir()
        if choise==5:
            papki()
        if choise==6:
            files()
        if choise==7:
            info()
        if choise==8:
            about()
        if choise==9:
            victorina1()
        if choise==10:
            account.check()
        if choise==11:
            cd(input('������� ��� �����'))
        if choise==12:
            break
        if choise==13:
            n=get_value('������� ��������? ')
            some_pic(pic_path,n)
        if choise==14:
            #save_list()
            gen_save_list()