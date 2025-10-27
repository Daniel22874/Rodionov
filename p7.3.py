a = int(input())
b = int(input())
li = [a, b]
minmax = [str(i) for i in range(min(li), max(li) + 1)]
maxmin = [str(i) for i in range(max(li), min(li) - 1, -1)]
print(' '.join(minmax))
print('\n'.join(maxmin))


p = int(input())
gruz = input().split(" ")
gruz = [int(m) for m in gruz]
summ_gruzov = sum(gruz)
if p > summ_gruzov:
	print('Перевозка грузов возможна')
else:
	print("Перевозка грузов невозможна")