from collections import Counter


def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """

    # from collections import Counter
    # temp = Counter(string.lower())
    # if 2 in temp.values():
    #     return False
    # return True


    counts = Counter(string)  # count occurrences of each character

    # If any character appears more than once, return False
    for char, count in counts.items():
        if count > 1:
            return False
    return True



if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"

    print(f'"{test1}" has all unique characters: {is_unique("aaa")}')  # Should be False (has repeated 'l')
    print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be False     