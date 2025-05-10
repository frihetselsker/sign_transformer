import csv

# Parameters
input_file = 'europarl-v10.ro-en.tsv'
lang1 = 'ro'
lang2 = 'en'

# Read header and get indices of selected columns
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter='\t')
    header = next(reader)
    idx1 = 0
    idx2 = 1

    # Open output files
    with open(f'{lang1}.txt', 'w', encoding='utf-8') as out1, open(f'{lang2}.txt', 'w', encoding='utf-8') as out2:
        for row in reader:
            if len(row) > max(idx1, idx2):
                out1.write(row[idx1] + '\n')
                out2.write(row[idx2] + '\n')
