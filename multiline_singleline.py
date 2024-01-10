# script to convert multi-line fasta file to single line

file = open('output2.fasta', 'r')  # multiline fasta file
file2 = open('single.fasta', 'w')
temp = ''

for line in file:
    if '>' in line:
        file2.write(temp  + '\n')
        file2.write('\n')
        file2.write(line.strip() + '\n')
        merged = ''
    if '>' not in line:
        seq = line.strip()
        merged += seq
        temp = merged
file2.write(merged)

file.close()
file2.close()
