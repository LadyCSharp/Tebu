from math import pi, sqrt, pow, hypot, sin, cos, fabs

def test_pow():
    assert pow(2,2)==4
    assert pow(3,2)==9
    for x in range(1,10):
        assert pow(x,2)==x*x

def test_sqrt():
    assert sqrt(0)==0
    assert sqrt(1)==1
    assert sqrt(4)==2
    

def test_pi():
    assert pi>3
    assert fabs(sin(pi))<0.00001
    assert fabs(cos(pi)+1)<0.00001  

def test_hypot():
    assert hypot(3,4)==5
    for x in range(-5,5):
        for y in range(-5,5):
            assert hypot(x,y)==sqrt(x**2+y**2)