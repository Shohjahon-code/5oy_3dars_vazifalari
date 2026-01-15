from collections import namedtuple

Book = namedtuple("Book", ["title","author", "pages"])


kitob = [
    Book("Instasteller", "Buton", 100),
    Book("Shum bola", "Hoshimov", 67),
    Book("Kapalak", "Utyin", 216),
    Book("Issiq hona", "Pushkin", 6)
]


maxs = max(kitob, key=lambda k: k.pages)
sums = sum(k.pages for k in kitob)
print(maxs,sums)