def NumberPeptidesWithGivenMass(mass : int):
    mass = int(mass)
    amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    counts = [0 for _ in range(0, mass+1)]
    counts[0] = 1
    for i in range(0, mass+1):
        for j in amino_acid_masses:
            if (i >= j):
                counts[i] += counts[i-j];
    return counts[mass]

def main():
    mass = input()

    res = NumberPeptidesWithGivenMass(mass)

    print(res)

if __name__ == "__main__":
    main()

