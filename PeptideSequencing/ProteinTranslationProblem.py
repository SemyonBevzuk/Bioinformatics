def CreateDictFile():
    f = open('RNA_codon_table.txt', 'r')
    l = (f.read()).split()
    f.close()
    f = open('RNA_codon_table_dict.txt', 'w')
    f.write('{')
    i = 0
    while i<len(l):
        if len(l[i+1]) != 1:
            f.write('\'' + l[i] + '\'' + ': ' + '\'\'' + ',\n')
            i = i + 1
        else:
            f.write('\'' + l[i] + '\'' + ': ' + '\'' + l[i + 1] + '\'' + ',\n')
            i = i + 2
    f.write('}')
    f.close()

def CreateRNACodonTable():
    table = {'AAA': 'K',
     'AAC': 'N',
     'AAG': 'K',
     'AAU': 'N',
     'ACA': 'T',
     'ACC': 'T',
     'ACG': 'T',
     'ACU': 'T',
     'AGA': 'R',
     'AGC': 'S',
     'AGG': 'R',
     'AGU': 'S',
     'AUA': 'I',
     'AUC': 'I',
     'AUG': 'M',
     'AUU': 'I',
     'CAA': 'Q',
     'CAC': 'H',
     'CAG': 'Q',
     'CAU': 'H',
     'CCA': 'P',
     'CCC': 'P',
     'CCG': 'P',
     'CCU': 'P',
     'CGA': 'R',
     'CGC': 'R',
     'CGG': 'R',
     'CGU': 'R',
     'CUA': 'L',
     'CUC': 'L',
     'CUG': 'L',
     'CUU': 'L',
     'GAA': 'E',
     'GAC': 'D',
     'GAG': 'E',
     'GAU': 'D',
     'GCA': 'A',
     'GCC': 'A',
     'GCG': 'A',
     'GCU': 'A',
     'GGA': 'G',
     'GGC': 'G',
     'GGG': 'G',
     'GGU': 'G',
     'GUA': 'V',
     'GUC': 'V',
     'GUG': 'V',
     'GUU': 'V',
     'UAA': '',
     'UAC': 'Y',
     'UAG': '',
     'UAU': 'Y',
     'UCA': 'S',
     'UCC': 'S',
     'UCG': 'S',
     'UCU': 'S',
     'UGA': '',
     'UGC': 'C',
     'UGG': 'W',
     'UGU': 'C',
     'UUA': 'L',
     'UUC': 'F',
     'UUG': 'L',
     'UUU': 'F',
     }
    return table

def TranslateRNAIntoAminoAcid(pattern):
    table = CreateRNACodonTable()
    peptide = ''
    for i in range(0, len(pattern)-2, 3):
        peptide += table.get(pattern[i:i+3])
    return peptide

def main():
    #CreateDictFile()

    pattern = input()
    peptide = TranslateRNAIntoAminoAcid(pattern)
    print(peptide)

if __name__ == "__main__":
    main()
