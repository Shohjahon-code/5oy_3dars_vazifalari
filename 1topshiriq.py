from collections import namedtuple

Students = namedtuple("Students", ["name", "age", "score"])

talaba = [
    ("Shoha", 16, 100),
    ("Ali", 17, 90),
    ("Vali", 15, 80),
    ("Guli", 13, 46),
    ("Eshmat", 12, 88)
]

for a in talaba:
    n = Students(*a)
    print(n.name,n.age,n.score)