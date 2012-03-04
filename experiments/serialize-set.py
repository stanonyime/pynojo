# -*- coding: utf-8 -*-
# $File: serialize-set.py
# $Date: Sun Mar 04 18:48:58 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

from clock import clock

import pickle, cPickle, json, cjson, marshal

data = set(range(10))

def test(lib, enc, dec, niter = 100000):
    with clock(lib + ' encode:'):
        for i in range(niter):
            s = enc(data)

    print lib, 'encode len:', len(s)

    with clock(lib + ' decode:'):
        for i in range(niter):
            d = dec(s)

    assert d == data


def myload(s):
    return set([int(i) for i in s.split('|')])

def mydump(s):
    return '|'.join([str(i) for i in s])

test('my', mydump, myload)
test('json', lambda s: json.dumps(list(s)), lambda s: set(json.loads(s)))
test('cjson', lambda s: cjson.encode(list(s)), lambda s: set(cjson.decode(s)))
test('pickle', 
        lambda s: pickle.dumps(s, pickle.HIGHEST_PROTOCOL),
        lambda s: pickle.loads(s))
test('cPickle', 
        lambda s: cPickle.dumps(s, cPickle.HIGHEST_PROTOCOL),
        lambda s: cPickle.loads(s))
test('marshal', marshal.dumps, marshal.loads)

