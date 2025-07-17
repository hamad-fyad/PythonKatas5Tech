def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    # """
    # if sentence == "":
    #     return 0
    # if sentence[-1] == " ":
    #     count = -1 
    # else :
    #     count = 1

    # for i in sentence:
    #     if i == " ":
    #         sentence = sentence.replace(" ", "")
    #         count += 1
    # return count


    return len(sentence.split())


if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed
