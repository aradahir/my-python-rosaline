input = 'AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB'
prob = [0.5]

AA = 0.194
AB = 0.806
BA = 0.273
BB = 0.727

for i in range(0,len(input)-1):
    if input[i] == 'A' and input[i+1] == 'A':
        prob.append(AA)
    elif input[i] == 'A' and input[i+1] == 'B':
        prob.append(AB)
    elif input[i] == 'B' and input[i+1] == 'A':
        prob.append(BA)
    else:
        prob.append(BB)

total_prob = 1
for j in prob:
    total_prob = total_prob* j

print(total_prob)
