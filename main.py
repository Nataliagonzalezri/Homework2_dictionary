from module_dictionary import possible_words


def translate_from_english_to_spanish(possible_words, input):
    """
    :param possible_words: the words in the dictionary
    :param input: the phrase the user writes
    :return: None, just prints
    """
    input_word_by_word = input.split()
    # print(input_word_by_word)
    translated_phrase = ""
    for word in input_word_by_word:
        if word not in possible_words.keys():
            print("At least one of your words is not in the dictionary")
        for word_in_english in possible_words.keys():
            if word == word_in_english:
                translated_word = possible_words[word_in_english]
                translated_phrase = translated_phrase + str(translated_word) + str(" ")
    return translated_phrase

user_phrase = input("Please enter a phrase of 3 words, one pronoun, one verb and one adjective: ")
print(translate_from_english_to_spanish(possible_words, user_phrase))
