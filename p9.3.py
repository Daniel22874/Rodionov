with open("res1.txt", "r", encoding='utf-8') as f:
    ch = f.read()
digits = '1234567890'
ch = ch.split("\n")
ch2 = []
for el in ch:
    for e in el:
        if e in digits and el not in ch2:
            ch2.append(el)
ch2 = [float(x) for x in ch2]
summ = sum(ch2)
maxi = max(ch2)
with open("res1.txt", "w", encoding='utf-8') as f:
    ch = [str(x) for x in ch]
    for el in ch:
        f.write(el + "\n")
    f.write(str(summ) + "\n")
    f.write(str(maxi))