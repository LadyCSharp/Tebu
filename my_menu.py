# This Python file uses the following encoding: Windows-1251
import os
import sys
import shutil
import platform 

# ������� ���������
# f - �������� �������
def add_separators(f):
    # inner - �������� ������� � ����� ���������
    def inner(*args, **kwargs):
        # ��������� �� ������
        print('*' * 10)
        result = f(*args, **kwargs)
        # ��������� ����� ������
        print('*' * 10)
        return result

    # ������������ ������� inner � ����� ����������
    return inner

@add_separators
def menu(menu_puncts):
    i=1
    for punct in menu_puncts:
        print(i,punct)
        i+=1
    choice=get_value("\n ")
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
@add_separators
def dir():
    for p in os.listdir():
        print(p)
@add_separators    
def papki():
    for p in os.listdir():
        if os.path.isdir(p):
            print(p)
@add_separators
def files():
    for p in os.listdir():
        if os.path.isfile(p):
            print(p)
def my_copy(name):
    if os.path.exists(name):
        shutil.copy(name, 'copy_'+name)


def info():
    print(platform.platform())

@add_separators   
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

def  gen_save_list():
    s='files:'
    s+=' '.join([p for p in os.listdir()  if os.path.isfile(p)])
    s+='\ndirs:'
    s+=' '.join([p for p in os.listdir() if os.path.isdir(p)])
    print(s)       
    with open('listdir1.txt', 'wt') as f:
        f.write(s)


def get_value(text):
    while True:
        try:
             v=int(input(text))
        except:
            print('��� �� �����')
        else:
            return v