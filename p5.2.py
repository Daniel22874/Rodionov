c = ("word", "first", "second", "third", "four", "first", "weather")
rand = "fly"
ind = []
for i in range(len(c)):
    if c[i] == rand:
        ind.append(i)
if len(ind) == 2:
    print(c[ind[0]:ind[1] + 1])
elif len(ind) == 1:
    print(c[ind[0]:])
else:
    print(())
    
        
    
