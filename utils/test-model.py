# -*- coding: utf-8 -*-
# $File: test-model.py
# $Date: Sun Mar 04 12:05:50 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

from os.path import isfile

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from pynojo.model import install_db
from pynojo.model.user import *
from pynojo.model.user.auth_pw import *
from pynojo.model.acl import *

#DBFILE = '/tmp/pynojo-test.db'
DBFILE = ':memory:'

if isfile(DBFILE):
    init = lambda *arg: None
else:
    def init(engine, ses):
        install_db(engine)

        g0 = UserGrpMdl(name = 'g0')
        g1 = UserGrpMdl(name = 'g1')
        u0 = UserMdl(username = 'user0')

        u0.groups.append(g0)
        u0.groups.append(g1)
        g0.perms.update([1, 2])
        g1.perms.update([2, 3])

        ses.add(u0)
        ses.commit()

engine = create_engine('sqlite:///' + DBFILE, echo = True, echo_pool = True)

event.listen(engine, 'connect', lambda con, record:
        con.execute('PRAGMA foreign_keys=ON'))

Session = sessionmaker(bind = engine)
ses = Session()

init(engine, ses)

del init

def test_raw():
    con = engine
    con.execute('delete from ugrp where id = 2')
    print con.execute('select gid, perm from mugrpperm').fetchall()

def test_orm():
    ses.query(UserGrpMdl).filter(UserGrpMdl.id == 2).delete()
    for i in ses.query(MapUserGrpAndGrpPerm).all():
        print 'gid', i.gid, 'perm', i.perm

def test_invcache():
    invalidate_user_perm_cache(ses, 2)

def test_expire_all():
    g = ses.query(UserGrpMdl).first()
    ses.expire_all()
    g.perms.add(3)
    ses.commit()
    ses.expire_all()
    g.perms.add(4)

def get_user():
    return ses.query(UserMdl).one()

import code
code.interact(local = locals())
