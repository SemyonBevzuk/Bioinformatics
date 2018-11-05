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

TableAminoAcidMass = CreateTableAminoAcidMass()
TableMassAminoAcid = CreateTableMassAminoAcid()

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

def LinearScore(peptide, spectrum):
    theoretical_spectrum = Linearspectrum(peptide)
    experimental_spectrum = []
    for i in spectrum:
        experimental_spectrum.append(int(i))

    score = 0
    i = 0
    j = 0
    while (i < len(theoretical_spectrum) and j < len(experimental_spectrum)):
        if (theoretical_spectrum[i] == experimental_spectrum[j]):
            i += 1
            j += 1
            score += 1
        else:
            if (theoretical_spectrum[i] < experimental_spectrum[j]):
                i += 1
            else:
                j += 1
    return score

def GetPeptideMass(peptide):
    mass = 0
    for c in peptide:
        mass += TableAminoAcidMass[c]
    return mass

def ParentMass(spectrum):
    return spectrum[-1]

def Expand(peptides):
    res = set()
    aminoacids = set({'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'Y'})

    if(len(peptides)==0):
        res = aminoacids
    else:
        for i in peptides:
            for j in aminoacids:
                res.add(i+j)
    return res

def Trim(n, Leaderboard, spectrum):
    res = set()
    peptide_score_list = []
    for i in Leaderboard:
        peptide_score_list.append([i, LinearScore(i, spectrum)])
    peptide_score_list = sorted(peptide_score_list, key = lambda element: element[1], reverse=True)
    min_length = min(len(peptide_score_list), int(n))
    flag = True
    add_count = 0
    while (flag):
        if (add_count < min_length):
            res.add(peptide_score_list[add_count][0])
            add_count += 1
        else:
            if(add_count < len(peptide_score_list) and peptide_score_list[min_length-1][1] == peptide_score_list[add_count][1]):
                res.add(peptide_score_list[add_count][0])
                add_count += 1
            else:
                flag = False

    return res

def LeaderboardCyclopeptideSequencing(n, spectrum_str):
    spectrum = []
    for i in spectrum_str.split():
        spectrum.append(int(i))

    flag = True
    Leaderboard = set()
    LeaderPeptid = ''
    while (len(Leaderboard) != 0 or flag):
        flag = False
        remove_peptides = []
        Leaderboard = Expand(Leaderboard)
        for p in Leaderboard:
            if (GetPeptideMass(p) == ParentMass(spectrum)):
                if (LinearScore(p, spectrum) > LinearScore(LeaderPeptid, spectrum)):
                    LeaderPeptid = p
            else:
                if (GetPeptideMass(p) > ParentMass(spectrum)):
                    remove_peptides.append(p)
        for p in remove_peptides:
            Leaderboard.remove(p)
        Leaderboard = Trim(n, Leaderboard, spectrum)

    return LeaderPeptid

def ConvertPeptidesToMasses(peptid):
    res_str = ''
    for i in peptid:
        res_str += str(TableAminoAcidMass[i]) + '-'
    return res_str[:-1]

def main():
    N = input()
    Spectrum = input()
    res = LeaderboardCyclopeptideSequencing(int(N), Spectrum)
    print(ConvertPeptidesToMasses(res))

if __name__ == "__main__":
    main()