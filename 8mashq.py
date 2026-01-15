matn = "Hello my friend.My name is Shokha. My number is 777"


h = 0
r = 0
b = 0
for a in matn:
    if a.isalpha():
        h+=1
    if a.isdigit():
        r +=1
    if a.isspace():
        b +=1

print(h,r,b)

