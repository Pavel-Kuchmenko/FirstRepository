import os

def get_name_of_current_script(name = "") -> str:
    for sign in __file__[::-1]:
        if sign == '\\':
            break
        name += sign
    return name

def get_files(except_file = get_name_of_current_script()) -> list:
    files = os.listdir()
    if len(files) == 1:
        print("No files in current folder except script!")
        return
    files.remove(except_file[::-1])
    return files

def get_all_words_from_file(received_file, words = list(), word_start_index = 0, word_end_index = 0, is_word = False) -> list:
    signs_list = [' ', '\n', '\t']
    file_stream = open(received_file).read()
    for index, value in enumerate(file_stream):
        if value not in signs_list and is_word == False:
            word_start_index = index
            is_word = True
        elif value in signs_list and is_word == False:
            continue
        elif value in signs_list and is_word == True:
            word_end_index = index-1
            words.append(file_stream[word_start_index:word_end_index])
            is_word = False
    return words

def get_lines_from_file(received_file, lines = list(), line = "") -> list:
    file_stream = open(received_file).read()
    for value in file_stream:
        if value == '\n':
            lines.append(line)
            line = ""
            continue
        line+=value
    return lines

def get_number_of_vowels(received_file, number_of_vowels = 0) -> int:
    vowels = 'aeiouy'
    received_file_stream = open(received_file).read()
    for value in received_file_stream:
        if value in vowels:
            number_of_vowels += 1
    return number_of_vowels

def get_number_of_consonants(received_file, number_of_consonants = 0) -> int:
    consonants = "bcdfghjklmnpqrstvwxyz"
    received_file_stream = open(received_file).read()
    for value in received_file_stream:
        if value in consonants:
            number_of_consonants += 1
    return number_of_consonants

def get_number_of_numbers(received_file, number_of_numbers = 0) -> int:
    numbers = "1234567890"
    received_file_stream = open(received_file).read()
    for value in received_file_stream:
        if value in numbers:
            number_of_numbers += 1
    return number_of_numbers

