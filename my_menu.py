# This Python file uses the following encoding: Windows-1251
import os
import sys
import shutil
import platform
def menu(menu_puncts):
    i=1
    for punct in menu_puncts:
        print(i,punct)
        i+=1
    choice=int(input())
    if choice <=0:
        choice=1
    if choice>len(menu_puncts):
        choice=len(menu_puncts)
    return choice
def new_fold(name):
    if not os.path.exists(name):
        os.mkdir(name)

def del_fold(name):
    if os.path.exists(name):
        os.rmdir(name)

def dir():
    for p in os.listdir():
        print(p)
    
def papki():
    for p in os.listdir():
        if os.path.isdir(p):
            print(p)
def files():
    for p in os.listdir():
        if os.path.isfile(p):
            print(p)
def my_copy(name):
    if os.path.exists(name):
        shutil.copy(name, 'copy_'+name)


def info():
    print(platform.platform())
    
def about():
    
    print('��� ��������� ������� ��������:\n ����� �������\n ������� ��������� \n �� ������� �����')
    
def cd(name):
    os.chdir(name)

def  save_list():
     with open('listdir.txt', 'wt') as f:
        f.write('files:')
        for p in os.listdir():
            if os.path.isfile(p):
                f.write(p+', ')
        f.write('\ndirs:')
        for p in os.listdir():
            if os.path.isdir(p):
               f.write(p+', ')