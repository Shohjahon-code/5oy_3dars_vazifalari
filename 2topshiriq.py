from collections import namedtuple

Product = namedtuple("Product", ["name", "price", "quantity"])



mahsulot = [
    ("Shoha", 100, 1),
    ("Ali", 1000000, 2),
    ("Vali", 15, 3),
    ("Guli", 200000, 4),
    ("Eshmat", 500000, 5)
]


for a in mahsulot:
    n = Product(*a)
    k = n.price * n.quantity
    if k > 100000:
        print(n.name, n.price, n.quantity)