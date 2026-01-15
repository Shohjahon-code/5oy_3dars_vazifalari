from collections import namedtuple

Movie = namedtuple("Movie", ["title", "reyting", "year"])

film = [
    ("Instasteller", 10, 2014),
    ("Shum bola", 8, 1990),
    ("Sehirli Qalpoqcha", 9, 2016),
    ("Himopyachi", 5, 2010)
]


for a in film:
    n = Movie(*a)
    if n.year > 2015 and n.reyting >= 8:
        print(n.title, n.reyting, n.year)