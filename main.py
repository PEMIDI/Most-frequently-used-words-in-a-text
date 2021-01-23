import operator
import re


def detect_words(txt):
    """
    this function define to detect words and insert words into a list
    :param txt: get a sample text from input
    :return: list of words exist in that text.
    """

    # convert all letter to lowercase
    lowercase_of_txt = txt.lower()

    # this regex define to detect words
    regex_of_detect_words = "[\']*[a-zA-Z]+[\']*[a-zA-Z]*"

    # find words from text and insert them to the list
    list_of_words = re.findall(regex_of_detect_words, lowercase_of_txt)

    return list_of_words


def counter_words(list_words):
    """

    :param list_words: get list of main words then count word repetition
    :return: a dictionary contains for
             key: word   value: repetition of that word
    """
    count_of_words_dict = dict()

    for word in list_words:
        if word in count_of_words_dict:
            count_of_words_dict[word] += 1
        else:
            count_of_words_dict[word] = 1

    return count_of_words_dict


def top_3_words(text):
    """
    this function define to
    detect most 3 frequencies of words that exist in text
    :param text: get sample text from user
    :return: most 3 frequencies of words that exist in text
    """

    # pass text to a this function to analyze words
    list_of_words = detect_words(text)

    # pass list of words to this function to count of words repetition
    words_count_dict = counter_words(list_of_words)

    # sorted words_count_dict and convert type to list for more access on it
    sorted_words_count_list = sorted(words_count_dict.items(),
                                     key=operator.itemgetter(1),
                                     reverse=True)

    # get length of that list to show a better result
    length_of_word_count_list = len(sorted_words_count_list)

    if length_of_word_count_list >= 3:
        final_list = [
            sorted_words_count_list[0][0],
            sorted_words_count_list[1][0],
            sorted_words_count_list[2][0]
        ]

    elif length_of_word_count_list == 2:
        final_list = [
            sorted_words_count_list[0][0],
            sorted_words_count_list[1][0]
        ]

    elif length_of_word_count_list == 1:
        final_list = [
            sorted_words_count_list[0][0]
        ]

    else:
        final_list = list()

    return final_list


if __name__ == '__main__':
    test1 = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

    test2 = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

    test3 = "  //wont won't won't"

    test4 = ""

    test5 = "  '''  "

    test6 = "  , e   .. "

    test7 = "  '  "

    top3word = top_3_words(test2)
    print(top3word)
