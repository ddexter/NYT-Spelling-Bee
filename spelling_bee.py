from sys import argv

primary_letter = None
letters = None


def is_valid(word):
    has_primary_letter = False
    for letter in word:
        if letter == primary_letter:
            has_primary_letter = True
        if letter not in letters:
            return False
    return has_primary_letter


def is_pentagram(word):
    return len(set(word)) >= 7


def main():
    with open('dictionary.txt') as dictionary:
        for line in dictionary:
            word = line.strip()
            if is_valid(word):
                if is_pentagram(word):
                    print('*** ' + word)
                else:
                    print(word)


if __name__ == '__main__':
    if len(argv) != 2:
        raise ValueError('Must input spelling bee letters')
    if len(argv[1]) != 7:
        raise ValueError('There must be exactly 7 spelling bee letters')

    letters = set([c for c in argv[1]])
    primary_letter = argv[1][0]

    main()
