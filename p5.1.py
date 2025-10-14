c = (34, 42, 580, 365, 12)
count = 0
for el in c:
    if type(el) is int:
        count += 1
if count == len(c):
    print(sorted(c))
else:
    print(c)
        
        
