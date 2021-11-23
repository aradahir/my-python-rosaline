input = 'AAAACCCGGT'
couple = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
output = ''
for i in input:
    output = output + couple[i]
print(output[::-1])