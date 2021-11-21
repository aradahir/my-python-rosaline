string_1 = 'GGGCCGTTGGT'
string_2 = 'GGACCGTTGAC'
count_of_mismatch = 0
for i,j in zip(string_1,string_2):
    if i != j:
        count_of_mismatch += 1

print(count_of_mismatch)