from my_menu import menu
from victo import rand_pers
import random
from account import *
pers={'Ада Лавлейс': '10.12.1815', 'Хеди Ламарр':'9.11.1914', 'Мария Склодовская-Кюри':'7.11.1867', 
          'Софья Васильевна Ковалевская':'3.01.1850', 'Адель Голдберг': '7.07.1945'}
def test_victorina():
    for i in range(1, len(pers)+1):
        assert len(rand_pers(pers,i))==i 
    for p in rand_pers(pers,3):
        assert p in pers.keys()
puncts='диван;чемодан;саквояж;картина;корзина;картонка;маленькая собачонка'.split(';')   
def test_menu(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda: random.choice([-1,1,5,15])) #
    m=menu(puncts)
    assert m>0 and m<=len(puncts)

def test_something_that_involves_user_input(monkeypatch): 
    # monkeypatch the "input" function, so that it returns "Mark". 
    # This simulates the user entering "Mark" in the terminal: 
    monkeypatch.setitem(__builtins__, 'input', lambda x: "Mark") # go about using input() like you normally would: 
    i = input("What is your name?") 
    assert i == "Mark" 

def test_put():
    assert put(0,random.choice([-1,1,5,15]))>=0

def test_shop():
    assert shop(300,random.choice([-100,100,50,1500]),'неведомая хрень')<=300