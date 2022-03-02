def f(name):    
    r = range(len(name))
    for i in r:
        for j in range(i,len(name)):
            print(name[i:j+1])

f("tamer")