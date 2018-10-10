def PatternCount(pattern, genome):
    count: int = 0
    pattern_len = len(pattern)
    genome_len = len(genome)
    if (pattern_len <= genome_len):
        for c in range(len(genome) - pattern_len + 1):
            if (genome[c:c + pattern_len] == pattern):
                count += 1
    return count


def main():
    pattern = input()
    genome = input()
    count = PatternCount(pattern, genome)
    print(count)


if __name__ == "__main__":
    main()
