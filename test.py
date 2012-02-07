from stooj.lib.enum import get_base
Base = get_base(start = 42, step = 8)

class Enum0(Base):
    VAL0 = Base.enum
    VAL1 = Base.enum
    VAL2 = 'str'

class Enum1(Enum0):
    VAL3 = Base.enum

class Enum2(Base):
    VAL4 = Base.enum
    VAL5 = Base.enum('hello, world')
    
print Enum0.VAL0, Enum0.VAL1, Enum0.VAL2
print Enum1.VAL3
print Enum2.VAL4
print Enum2.get_data(Enum2.VAL5)

