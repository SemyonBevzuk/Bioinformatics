import sys

def CalculateProbablity(profile, kmer):
    prob = 1
    for i in range(0, len(kmer)):
        if kmer[i] == 'A':
            prob = prob * profile[0][i]
        elif kmer[i] == 'C':
            prob = prob * profile[1][i]
        elif kmer[i] == 'G':
            prob = prob * profile[2][i]
        elif kmer[i] == 'T':
            prob = prob * profile[3][i]
    return prob

def ProfileMostProbable(dna, k, profile):
    best_pattern = dna[0:0 + k]
    best_probability = 0.0
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i + k]
        new_probablity = CalculateProbablity(profile, kmer)
        if new_probablity > best_probability:
            best_pattern = kmer
            best_probability = new_probablity
    return best_pattern

def CreateProfilePseudocounts(motifs):
    n = 4
    m = len(motifs[0])
    profile = [[1] * m for i in range(n)]

    for i in range(len(motifs)):
        for j in range(len(motifs[i])):
            if motifs[i][j] == 'A':
                profile[0][j] += 1
            if motifs[i][j] == 'C':
                profile[1][j] += 1
            if motifs[i][j] == 'G':
                profile[2][j] += 1
            if motifs[i][j] == 'T':
                profile[3][j] += 1

    for i in range(n):
        for j in range(m):
            profile[i][j] = profile[i][j]/(len(motifs)+4)

    return profile

def Score(motifs):
    score = 0
    for j in range(len(motifs[0])):
        count = 0
        counts = [0, 0, 0, 0]
        for i in range(len(motifs)):
            if motifs[i][j] == 'A':
                counts[0] += 1
                count += 1
            if motifs[i][j] == 'C':
                counts[1] += 1
                count += 1
            if motifs[i][j] == 'G':
                counts[2] += 1
                count += 1
            if motifs[i][j] == 'T':
                counts[3] += 1
                count += 1
        score += count - max(counts)
    return score

def GreedyMotifSearchWhithPseudocounts(dna, k, t):
    BestMotifs = []
    for i in range(t):
        BestMotifs.append(dna[i][0:k])

    for i in range(len(dna[0]) - k + 1):
        Motifs = []
        Motifs.append(dna[0][i:i + k])

        for j in range(1, t):
            Profile = CreateProfilePseudocounts(Motifs)
            Motifs.append(ProfileMostProbable(dna[j], k, Profile))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs.copy()
    return BestMotifs

def PrintMotif(motif):
    for i in motif:
        print(i)

def main():

    k, t = input().split()
    dna = sys.stdin.read().split('\n')
    '''
    k = 5
    t = 5
    dna = ['GCCAGATCCAATGACGGCTCCGCCAGAATCTGACA',
           'AAAGGCATAGTCGAATATGCCGACAGGTTTGAGTT',
           'ACTTCGGTCGCGATACCCGCAAGGAGTACCCCGAG',
           'CCTCGTAGGGGCGAACCTCAGAAGGCTACAAGACA',
           'ATTGGTGATATTGAGCGGTGCCTGAGGATCATCCT']
    '''
    res = GreedyMotifSearchWhithPseudocounts(dna, int(k), int(t))
    PrintMotif(res)

if __name__ == "__main__":
    main()
