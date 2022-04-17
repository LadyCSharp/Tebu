import numpy as np

def test_filter():
    l=np.arange(-10,10,1)
    for el in filter(lambda x:x%2==0, l):
        assert (el in l)==True
        assert el%2==0
    for el in filter(lambda x:x<=0, l):
        assert el in l
        assert el<=0

def test_map():
    l=np.arange(-10,10,1)
    for el in map(lambda x:abs(x), l):
        assert el>=0
        assert (el in l) or (-el in l)

def test_sorted():
    l=np.random.randint(-10,10,size=10)
    assert len(sorted(l))==len(l)
    for el in l:
        assert el in sorted(l)
    for el in sorted(l):
        assert el in l
