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

def FindBestProbablityPattern(text, k, profile):
    best_pattern = ""
    best_probability = 0.0
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        new_probablity = CalculateProbablity(profile, kmer)
        if new_probablity > best_probability:
            best_pattern = kmer
            best_probability = new_probablity
    return best_pattern

def main():

    text = input()
    k = input()
    profile = []
    for i in range(0,4):
        profile.append([float(j) for j in input().split()])

    #text = 'CCCCTATAGTTCTTGGTGCAGCGTGCACCCTCGTCTGGTTCGGATACGGGCCTGCCAGGA'
    #k = 5
    #profile =[[0.583, 0.25, 0.417, 0.25, 0.167],
    #          [0.083, 0.25, 0.417, 0.333, 0.25],
    #          [0, 0.25, 0.167, 0, 0.333],
    #          [0.333, 0.25, 0, 0.417, 0.25]]

    res = FindBestProbablityPattern(text, int(k), profile)
    print(res)

if __name__ == "__main__":
    main()
