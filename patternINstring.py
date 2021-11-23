pattern = 'ATAT'
genome = 'GATATATGCATATACTT'
result = []
for i in range(0, len(genome)-len(pattern)+1):
    if pattern == genome[i:i+4]:
        result.append(i)

print(result)