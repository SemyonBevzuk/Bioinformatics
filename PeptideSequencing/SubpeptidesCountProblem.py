def FindNumberOfSubpeptides(length_cyclic_peptide):
    return int(length_cyclic_peptide)*(int(length_cyclic_peptide)-1)

def main():
    length_cyclic_peptide = input()

    res = FindNumberOfSubpeptides(length_cyclic_peptide)

    print(res)

if __name__ == "__main__":
    main()
