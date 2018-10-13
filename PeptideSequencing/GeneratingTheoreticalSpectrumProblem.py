def CreateTableAminoAcidMass():
    table = {
     'G': 57,
     'A': 71,
     'S': 87,
     'P': 97,
     'V': 99,
     'T': 101,
     'C': 103,
     'I': 113,
     'L': 113,
     'N': 114,
     'D': 115,
     'K': 128,
     'Q': 128,
     'E': 129,
     'M': 131,
     'H': 137,
     'F': 147,
     'R': 156,
     'Y': 163,
     'W': 186 }
    return table

def FixPeptide(peptide):
    TableAminoAcidMass = CreateTableAminoAcidMass()
    res = ''
    for c in peptide:
        if TableAminoAcidMass.get(c) != None:
            res += c
    return res


def Cyclospectrum(peptide):
    peptide = FixPeptide(peptide)
    TableAminoAcidMass = CreateTableAminoAcidMass()
    res = []
    i = 0
    k = 1
    while k < len(peptide):
        while i < len(peptide):
            j = 0
            tmp = 0
            while j < k:
                tmp += int(TableAminoAcidMass.get(peptide[(i + j) % len(peptide)]))
                j += 1
            res.append(tmp)
            i += 1
        i = 0
        k += 1
    if len(peptide) != 0:
        tmp = 0
        for c in peptide:
            tmp += int(TableAminoAcidMass.get(c))
        res.append(tmp)
        res.append(0)
    res.sort()
    string = ''
    for i in res:
        string += str(i) + ' '
    return string[:-1]

def main():
    peptide = input()

    res = Cyclospectrum(peptide)

    print(res)

if __name__ == "__main__":
    main()
