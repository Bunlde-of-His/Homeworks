def spam(number):
    bulka_str = 'bulochka' * number
    return bulka_str


def my_sum(list_of_numbers):
    my_result = 0
    for element in list_of_numbers:
        my_result += element
    return my_result



def shortener(string):
    words_in_sentence = string.split()
    for letter in range(len(words_in_sentence)):
        if len(words_in_sentence[letter]) > 6:
            words_in_sentence[letter] = words_in_sentence[letter][:6] + '*'
    return ' '.join(words_in_sentence)






def compare_ends(words):
    my_start = 0
    for element in words:
        if len(element) >= 2 and element[0] == element[-1]:
            my_start += 1
    return my_start

