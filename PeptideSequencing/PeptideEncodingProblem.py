from collections import defaultdict

def ComplementarityRule(symbol):
    # A=T C=G
    if (symbol == 'A'):
        return 'T'
    elif (symbol == 'T'):
        return 'A'
    elif (symbol == 'C'):
        return 'G'
    elif (symbol == 'G'):
        return 'C'
    else:
        print('Not found!')
        return ' '

def TranscribedRNA(pattern):
    result = ''
    for c in pattern:
        if (c == 'T'):
            result += 'U'
        else:
            result += c
    return result

def UnTranscribedRNA(pattern):
    result = ''
    for c in pattern:
        if (c == 'U'):
            result += 'T'
        else:
            result += c
    return result

def ReverseComplement(pattern):
    reverse_complement = ''
    for c in pattern:
        reverse_complement += ComplementarityRule(c)
    return reverse_complement[::-1]

def CreateTableRNA_Peptide():
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
def CreateTablePeptide_RNA(table):
    result_table = defaultdict(list)
    for key, value in table.items():
        result_table[value].append(key)
    return result_table

def TranslateRNAIntoAminoAcid(pattern):
    table = CreateTableRNA_Peptide()
    peptide = ''
    for i in range(0, len(pattern)-2, 3):
        peptide += table.get(pattern[i:i+3])
    return peptide

def FindPeptideInDNA(dna, peptide):
    len_peptide = len(peptide) * 3
    i = 0;
    res = []
    while i < len(dna) - len_peptide + 1:
        string = dna[i:i + len_peptide]
        if TranslateRNAIntoAminoAcid(TranscribedRNA(string)) == peptide:
            res.append(string)
        i += 1
    dna = ReverseComplement(dna)
    i = 0
    while i < len(dna) - len_peptide + 1:
        string = dna[i:i + len_peptide]
        if TranslateRNAIntoAminoAcid(TranscribedRNA(string)) == peptide:
            res.append(ReverseComplement(string))
        i += 1
    words = ''
    for i in res:
        words += i + ' '
    #print(words)
    return words[:-1]

def main():
    dna = input()
    peptide = input()

    res = FindPeptideInDNA(dna, peptide)

    print(res)

if __name__ == "__main__":
    main()
