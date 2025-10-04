text = input().lower()
d = dict()
for i in range(len(text)):
    d[text[i]] = text.count(text[i])
d2 = sorted(d.items(), key=lambda item: -item[1])
res = d2[:3]
for el in res:
    el = [str(x) for x in el]
    print(" - ".join(el))