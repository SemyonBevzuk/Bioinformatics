def PatternCount(pattern, genome):
    count: int = 0
    pattern_len = len(pattern)
    genome_len = len(genome)
    if (pattern_len <= genome_len):
        for c in range(len(genome) - pattern_len + 1):
            if (genome[c:c + pattern_len] == pattern):
                count += 1
    return count

def FrequentWords(text, k):
    FrequentPatterns = []
    Patterns = {}
    size_pattern = int(k)
    maxCount = 0
    for i in range(len(text) - size_pattern):
        pattern = text[i: i + size_pattern]
        count = PatternCount(pattern, text)
        Patterns[pattern] = count
        if (count > maxCount):
            maxCount = count
    for i in Patterns:
        if (Patterns[i] == maxCount):
            FrequentPatterns.append(i)
    FrequentPatterns.sort()
    words = ' '.join(FrequentPatterns)
    return words


def main():
    text = input()
    k = input()
    words = FrequentWords(text, k)
    print(words)


if __name__ == "__main__":
    main()
