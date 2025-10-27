def f(x):
	if x >= 0:
		return round(x ** 0.5 + x ** 2, 2)
	else:
		return round(1 / x, 2)


def maxmin(d1, d2):
	li = [d1, d2]
	return f"""Максимальное: {max(li)}
Минимальное: {min(li)}"""


print(f(10))
print(maxmin(23, -145))
