from collections import namedtuple

Book = namedtuple("Book", ["title","author", "pages"])


kitob = [
    ("Instasteller", "Buton", 100),
    ("Shum bola", "Hoshimov", 67),
    ("Kapalak", "Utyin", 216),
    ("Issiq hona", "Pushkin", 6)
]


n = [Book(*a).pages for a in kitob]
print(max(n))
print(sum(n))