with open("poem.txt", "r", encoding='utf-8') as f:
	stix = f.read()
	print(stix)
	print("  ")
gl = "уеэоаыяию"
sogl = "йцкнгшщзхждлрпвфчсмтб"
stix = stix.replace("\n", " ")
stix = stix.split(" ")
c_gl = 0
c_sogl = 0
for el in stix:
	if el[0] in gl:
		c_gl += 1
	if el[0] in sogl:
		c_sogl += 1
if c_gl > c_sogl:
	print("Слов с 1 гласной больше")
elif c_gl < c_sogl:
	print("Слов с 1 согласной больше")
else:
	print("Кол-во слов с 1 гласной и 1 согласной одинаково")