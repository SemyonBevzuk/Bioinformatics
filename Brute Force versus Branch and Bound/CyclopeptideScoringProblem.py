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

TableAminoAcidMass = CreateTableAminoAcidMass()

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

def Score(peptide, spectrum):
    theoretical_spectrum = Cyclospectrum(peptide)
    experimental_spectrum = []
    for i in spectrum.split():
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

def main():
    Peptide = input()
    Spectrum = input()
    res = Score(Peptide, Spectrum)
    print(res)

if __name__ == "__main__":
    main()