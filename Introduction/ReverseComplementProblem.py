def ComplementarityRule(symbol):
    # A=T C=G
    if (symbol == 'A'):
        return 'T'
    elif (symbol == 'T'):
        return 'A'
    elif (symbol == 'C'):
        return 'G'
    elif (symbol == 'G'):
        return 'C'
    else:
        print('Not found!')
        return ' '

def ReverseComplement(pattern):
    reverse_complement = ''
    for c in pattern:
        reverse_complement += ComplementarityRule(c)
    return reverse_complement[::-1]

def main():
    pattern = input()
    reverse_complement_pattern = ReverseComplement(pattern)
    print(reverse_complement_pattern)

if __name__ == "__main__":
    main()
