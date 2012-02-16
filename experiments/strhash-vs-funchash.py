# $File: strhash-vs-funchash.py
# $Date: Thu Feb 16 15:53:12 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

from clock import clock

NITER = 10000000

DATA0 = {1:2, 3:4, 5:6, 7:8}

def test_func():
    data = DATA0.copy()
    with clock('func'):
        for i in range(NITER):
            data[test_func] = 0


def test_str():
    data = DATA0.copy()
    with clock('str'):
        for i in range(NITER):
            data['test_func'] = 0

def test_str_var():
    data = DATA0.copy()
    s = 'test_func'
    with clock('str var'):
        for i in range(NITER):
            data[s] = 0

test_func()
test_str()
test_str_var()

