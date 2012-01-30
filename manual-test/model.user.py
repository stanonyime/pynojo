from stooj.model import install_db
from stooj.model.user import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo = True)
Session = sessionmaker(bind = engine)
install_db(engine)

import code
code.interact(local = locals())
