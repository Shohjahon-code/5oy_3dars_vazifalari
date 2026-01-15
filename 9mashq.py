new = []
for a in range(1,101):
    if a % 5==0 and a % 3!=0:
        new.append(a)
print(new)



## 2 usul
# r = range(1,101)
# n = list(filter(lambda x:x%5==0 and x%3!=0, r))
# print(n)