from collections.abc import Hashable

se = set()
li = ["weathers", 24, True, ["beefhfh"], {23, 54, 75}, (12, 55, 90)]
for el in li:
    if isinstance(el, Hashable):
        se.add(el)
print(se)
