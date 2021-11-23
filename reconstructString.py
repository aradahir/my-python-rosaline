genome = ['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']
result = genome[0]
for i in range(0,len(genome)-1):
    for j in range(0,len(genome[0])):
        if genome[i][j:len(genome[i])] == genome[i+1][0: len(genome[i])-j]:
            result = result + genome[i+1][len(genome[i])-j]
            print(result)
            break
           