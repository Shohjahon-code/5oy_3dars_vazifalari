from collections import namedtuple

Flight = namedtuple("Flight", ["from_city", "to_city", "duration"])

parvoz = [
    ("Fergana", "Tashkent", 5),
    ("Fergana", "Rishtan", 1),
    ("Fergana", "Xorazm", 9),
    ("Fergana", "Quvasoy", 1)
]
s = 0
for a in parvoz:
    n = Flight(*a)
    if n.duration >= 2:
        print(n.from_city, n.to_city, n.duration)
    s += n.duration
        
print(s)