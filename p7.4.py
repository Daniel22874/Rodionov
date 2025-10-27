s = 0
c = 0
while True:
	n = int(input())
	s += n
	c += 1
	if n == 0:
		print(f"Сумма: {s}")
		print(f"Количество: {c}")
		break
