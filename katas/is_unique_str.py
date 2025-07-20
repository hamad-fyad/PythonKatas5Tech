def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """
<<<<<<< HEAD
    # from collections import Counter
    # temp = Counter(string.lower())
    # if 2 in temp.values():
    #     return False
    # return True

    return len(string) == len(set(string.lower()))

=======
    
    
    return True
>>>>>>> 8ba878a992da4a9765868416a660e5da0f9fe598


if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"

    print(f'"{test1}" has all unique characters: {is_unique("aaa")}')  # Should be False (has repeated 'l')
    print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be False     