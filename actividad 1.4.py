lista = ["a","b","c","d"]
for x in range(len(lista)):
    for y in range(x+1,len(lista)):
        for z in range(y+1,len(lista)):
            print(lista[x],lista[y],lista[z])