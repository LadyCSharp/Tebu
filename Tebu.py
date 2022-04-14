# This Python file uses the following encoding: Windows-1251

from my_menu import *
from two_pic import some_pic
#from account import check
import account
menu_puncts='- создать папку;- удалить (файл/папку);- копировать (файл/папку);- просмотр содержимого рабочей директории;- посмотреть только папки;- посмотреть только файлы;- просмотр информации об операционной системе;- создатель программы;- играть в викторину;- мой банковский счет;- смена рабочей директории (*необязательный пункт);- выход.'.split(';')

while True:
    choise=menu(menu_puncts)
    if choise==1:
        new_fold(input('Введите имя папки'))
    if choise==2:
        del_fold(input('Введите имя'))    
    if choise==3:
        my_copy(input('Введите имя'))
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
    if choise==10:
        account.check()
    if choise==11:
        cd(input('Введите имя папки'))
    if choise==12:
        break
    if choise==13:
        some_pic(r'G:\Disk D\!!!lab\students\pictures',5)