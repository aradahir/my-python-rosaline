genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
dict_count = {}
for i in range(0, len(genome)-k+1):
    if genome[i:i+4] in dict_count:
        dict_count[genome[i:i+4]] += 1
    else:
        dict_count[genome[i:i+4]] = 1

sorting = sorted(dict_count.items(), key=lambda x: x[1], reverse=True)
max_value = sorting[0][1]
result = []
for j in range(0, len(sorting)-1):
    if sorting[j][1] < max_value:
        break
    result.append(sorting[j][0])
print(result)