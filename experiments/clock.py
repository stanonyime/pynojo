# $File: clock.py
# $Date: Fri Feb 10 11:04:38 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

import time
from contextlib import contextmanager

@contextmanager
def clock(msg = 'done:'):
    start = time.clock()
    yield
    print msg, time.clock() - start, '[sec]'

