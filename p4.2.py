first = ['fhfehe', 'fehejhefhhjrehjrhje', 'ghhtghtt']
res = []
lens_word = []
for el in first:
    lens_word.append(len(el))
max_len = max(lens_word)
for el in first:
    if len(el) != max_len:
        res.append(el + "_" * (max_len - len(el)))
    else:
        res.append(el)
print(res)
for el in res:
    print(len(el))
