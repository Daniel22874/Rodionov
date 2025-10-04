ch1 = int(input())
ch2 = int(input())
print(f'{ch1} + {ch2} = {ch1 + ch2}')
print(f'{ch1} - {ch2} = {ch1 - ch2}')
print(f'{ch1} * {ch2} = {ch1 * ch2}')
print(f'{ch1} / {ch2} = {round(ch1 / ch2, 3)}')
print(f'{ch1} // {ch2} = {ch1 // ch2}')
print(f'{ch1} % {ch2} = {ch1 % ch2}')
print(f'{ch1} ** {ch2} = {ch1 ** ch2}')
if ch1 < ch2:
    print(f'{ch1} < {ch2}')
if ch1 > ch2:
    print(f'{ch1} > {ch2}')
if ch1 == ch2:
    print(f'{ch1} = {ch2}')
