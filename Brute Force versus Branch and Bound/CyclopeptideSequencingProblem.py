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
     'W': 186}
    return table

def CreateTableMassAminoAcid():
    table = {
        57: 'G',
        71: 'A',
        87: 'S',
        97: 'P',
        99: 'V',
        101: 'T',
        103: 'C',
        113: 'I',
        114: 'N',
        115: 'D',
        128: 'K',
        129: 'E',
        131: 'M',
        137: 'H',
        147: 'F',
        156: 'R',
        163: 'Y',
        186: 'W'}
    return table

# таблицы масс и аминокислот
TableAminoAcidMass = CreateTableAminoAcidMass()
TableMassAminoAcid = CreateTableMassAminoAcid()

def Cyclospectrum(peptide):
    res = []
    i = 0
    k = 1
    while k < len(peptide):
        while i < len(peptide):
            j = 0
            tmp = 0
            while j < k:
                tmp += int(TableAminoAcidMass[peptide[(i + j) % len(peptide)]])
                j += 1
            res.append(tmp)
            i += 1
        i = 0
        k += 1
    if len(peptide) != 0:
        tmp = 0
        for c in peptide:
            tmp += int(TableAminoAcidMass[c])
        res.append(tmp)
        res.append(0)
    res.sort()
    return res

def Linearspectrum(peptide):
    res = []
    i = 0
    k = 1
    while k < len(peptide):
        while i < len(peptide)-k+1:
            j = 0
            tmp = 0
            while j < k:
                tmp += int(TableAminoAcidMass[peptide[i + j]])
                j += 1
            res.append(tmp)
            i += 1
        i = 0
        k += 1
    if len(peptide) != 0:
        tmp = 0
        for c in peptide:
            tmp += int(TableAminoAcidMass[c])
        res.append(tmp)
        res.append(0)
    res.sort()
    return res

def GetPeptideMass(peptide):
    mass = 0
    for c in peptide:
        mass += TableAminoAcidMass[c]
    return mass

def ParentMass(spectrum):
    return spectrum[-1]

def IsConsistent(peptide, spectrum):
    for p in Linearspectrum(peptide):
        if p not in spectrum:
            return False
    return True

def Expand(peptides, aminoacids):
    res = set()

    if(len(peptides)==0):
        res = aminoacids
    else:
        for i in peptides:
            for j in aminoacids:
                res.add(i+j)
    return res


def CyclopeptideSequencing(spectrum_str):
    spectrum = []
    for i in spectrum_str.split():
        spectrum.append(int(i))
    spectrum_set = frozenset(spectrum)
    aminoacids = set({'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'Y'})
    res = []

    flag = True
    Peptides = set()
    while(len(Peptides) != 0 or flag):
        flag = False
        remove_peptides = []
        Peptides = Expand(Peptides, aminoacids)
        for p in Peptides:
            if (GetPeptideMass(p) == ParentMass(spectrum)):
                if (Cyclospectrum(p) == spectrum):
                    res.append(p)
                remove_peptides.append(p)
            else:
                if not IsConsistent(p, spectrum_set):
                    remove_peptides.append(p)
        for p in remove_peptides:
            Peptides.remove(p)

    return res

def ConvertPeptidesToMasses(peptids):
    peptids.sort()
    res_str = ''
    for peptid in peptids:
        tmp = ''
        for i in peptid:
            tmp += str(TableAminoAcidMass[i])+'-'
        res_str += tmp[:-1] + ' '

    return res_str[:-1]

def main():
    spectrum = input()
    res_peptids = CyclopeptideSequencing(spectrum)
    print(ConvertPeptidesToMasses(res_peptids))

if __name__ == "__main__":
    main()