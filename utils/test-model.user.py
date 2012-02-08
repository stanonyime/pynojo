from pynojo.model import install_db
from pynojo.model.user import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo = True)
Session = sessionmaker(bind = engine)
install_db(engine)

g0 = UserGroup(name = 'g0')
u0 = User(username = 'u0')
ses = Session()

import code
code.interact(local = locals())
