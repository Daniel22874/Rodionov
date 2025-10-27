st = input().split(" ")
with open("res1.txt", "w", encoding='utf-8') as f:
	for ch in st[:-1]:
		f.write(ch + "\n")
	f.write(st[-1])