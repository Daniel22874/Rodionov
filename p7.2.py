n = int(input())
s = 0
c = 0
while n != 0:
	s += n
	c += 1
	n = int(input())
if n == 0:
	print(f"Сумма: {s}")
	print(f"Количество: {c + 1}")


N = int(input())
for i in range(0, N + 1, 5):
	print(i)