football = input()
print(f'{football} - чемпион!')
print('-' * len(football))
football = football.lower()
print(football)
print(len(football))
if "п" in football:
    print(True)
else:
    print(False)
print(football.lower().count("а"))
