from collections import namedtuple
from datetime import datetime

Person = namedtuple("Person", ["first_name", "last_name", "birth_year"])

odam = [
    ("Ali", "Aliyev", 2010),
    ("Vali", "Valiyev", 2009),
    ("Shoh", "Rahimov", 2007),
    ("Guli", "Guliyeva", 2008)
]



yil = datetime.now().year
for a in odam:
    n = Person(*a)
    h = max(odam, key=lambda x: yil-x[2])
print(h)
   