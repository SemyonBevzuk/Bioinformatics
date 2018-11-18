import sys

def HammingDistance(word_1, word_2):
    count_different_charts = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count_different_charts += 1
    return count_different_charts

def FindPatternFromNumber(num, k):
    NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    pattern = ''
    tmp_num = num
    while(len(pattern) != k):
        pattern += NumberToSymbol[tmp_num % len(NumberToSymbol)]
        tmp_num = tmp_num // len(NumberToSymbol)
    return pattern

def DistancePatternText(pattern, dna):
    k = len(pattern)
    distance = 0
    for string_dna in dna:
        min_distance_string = float('inf')
        for i in range(len(string_dna) - k + 1):
            d = HammingDistance(pattern, string_dna[i:i + k])
            if d < min_distance_string:
                min_distance_string = d

        distance += min_distance_string
    return distance

def MedianString(dna, k):
    distance = float('inf')
    median = ''
    for i in range(4 ** k):
        pattern = FindPatternFromNumber(i, k)
        d = DistancePatternText(pattern, dna)
        if distance > d:
            distance = d
            median = pattern
    return median

def main():
    k = input()
    dna = sys.stdin.read().split('\n')

    res = MedianString(list(dna), int(k))
    print(res)

if __name__ == "__main__":
    main()
