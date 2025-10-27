with open("res1.txt", "r", encoding='utf-8') as f:
    ch = f.read()
ch = ch.split("\n")
ch = [float(x) for x in ch]
summ = sum(ch)
maxi = max(ch)
with open("res1.txt", "w", encoding='utf-8') as f:
    ch = [str(x) for x in ch]
    for el in ch:
        f.write(el + "\n")
    f.write(str(summ) + "\n")
    f.write(str(maxi))