from sys import argv


def is_standard_alphabet(word):
    for c in word:
        index = ord(c) - 97
        if index < 0 or index > 25:
            return False
    return True


def main(infile, outfile):
    with open(infile) as dictionary, open(outfile, 'w+') as culled_dictionary:
        for line in dictionary:
            word = line.strip()
            if word.islower() and word.isalpha() and word.isascii and len(word) > 3 and is_standard_alphabet(word):
                culled_dictionary.write(word + '\n')


if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError('Must input name of dictionary and output path for words.')

    main(argv[1], argv[2])
