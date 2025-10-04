word = input()
symbol = input()
li = []
for i in range(len(word)):
    if word[i] == symbol:
        li.append(i)
if len(li) > 0:
    print(li[0], li[-1])
elif len(li) == 0:
    print("Чувак, такой буквы нет")