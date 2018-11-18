import sys

def HammingDistance(word_1, word_2):
    count_different_charts = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count_different_charts += 1
    return count_different_charts

def FindNeighboringMutations(Pattern, d):
    if len(Pattern) == 1:
        return ["A", "C", "G", "T"]

    neighbors = []
    suffix_neighbors = FindNeighboringMutations(Pattern[1:], d)

    for string in suffix_neighbors:
        if (HammingDistance(Pattern[1:], string) < d):
            for char in ["A", "C", "G", "T"]:
                neighbors.append(char+string)
        else:
            neighbors.append(Pattern[0]+string)

    return neighbors

def IsPatternInStringWhithMistakes(pattern, string_dna, d):
    k = len(pattern)
    for i in range(len(string_dna) - k + 1):
        dnaPattern = string_dna[i:i + k]
        if (HammingDistance(pattern, dnaPattern) <= d):
            return True
    return False

def ConvertMotifListToString(motif):
    res_str = ''
    for i in motif:
        res_str += str(i) + ' '
    return res_str[:-1]

def MotifEnumeration(dna, k, d):
    Patterns = []
    for string_dna in dna:
        for start_pattern in range(len(dna[0])-k+1):
            pattern = string_dna[start_pattern:start_pattern+k]
            mutations = FindNeighboringMutations(pattern, d)
            for mutation in mutations:
                IsMeetMutationInDna = True
                for i in range(len(dna)):
                    if IsPatternInStringWhithMistakes(mutation, dna[i], d) == False:
                        IsMeetMutationInDna = False
                        break
                if IsMeetMutationInDna:
                    Patterns.append(mutation)

    Patterns = set(Patterns)
    Patterns = list(sorted(Patterns))
    return ConvertMotifListToString(Patterns)

def main():
    k, d = input().split()
    dna = sys.stdin.read()
    res = MotifEnumeration(dna, int(k), int(d))
    print(res)

if __name__ == "__main__":
    main()
