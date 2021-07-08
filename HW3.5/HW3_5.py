from os import write
import HW3_5_help_funcs as HW3

#======================================= Task #1 =======================================
def compare_lines_of_files(file_1 = None, file_2 = None, compare_indexes = list()) -> None:
    if file_1 == None or file_2 == None:
        print("Do not received files!")
    file_1_lines = HW3.get_lines_from_file(file_1)
    file_2_lines = HW3.get_lines_from_file(file_2)
    for index, value in enumerate(file_1_lines):
        if value in file_2_lines:
            compare_indexes.append(index)
    if len(compare_indexes) == len(file_1_lines) or len(compare_indexes) == len(file_2_lines):
        print("Files are identical.")
    elif len(file_1_lines) == len(file_2_lines):
        print("Different lines:")
        for value in range(0,len(file_2_lines)-1):
            if value in compare_indexes:
                continue
            print(f"Line {value}: {file_1_lines[value]} from File #1")
            print(f"Line {value}: {file_2_lines[value]} from File #2")
    else:
        for value in range(0, len(file_1_lines)-1):
            if value in compare_indexes:
                continue
            print(f"Line {value}: {file_1_lines[value]} from File #1")
        for value in range(0, len(file_2_lines)-1):
            if value in compare_indexes:
                continue
            print(f"Line {value}: {file_2_lines[value]} from File #2")
#======================================= Task #2 =======================================
def make_file_with_params(received_file) -> None:
    params = [
        {"Length": len(open(received_file).read())},
        {"Lines amount": HW3.get_lines_from_file(received_file = received_file)},
        {"Vowels": HW3.get_number_of_vowels(received_file)},
        {"Сonsonants": HW3.get_number_of_consonants(received_file = received_file)},
        {"Numbers": HW3.get_number_of_numbers(received_file = received_file)}
    ]
    param_file = open(str(received_file.__name__).replace(".txt", "_params.txt"), 'w')
    for value in params:
        param_file.write(str(value).replace('{', '')+'\n')
    param_file.close()
#======================================= Task #3 =======================================    
def delete_last_line(received_file) -> None:
    lines = open(received_file).readlines()
    new_file = open(str(received_file.__name__).replace(".txt", "_new.txt"), "w")
    for value in range(0,len(list)-1):
        new_file.write(value)
#======================================= Task #4 =======================================   
def get_longest_line_length(received_file, longest_line_index = 0) -> int:
    lines = open(received_file).readlines()
    longest_line_index = lines[0]
    for value in range(1,len(lines)-1):
        if len(lines[value]) > len(lines[value-1]):
            longest_line_index = value
    return len(lines[longest_line_index])
#======================================= Task #5 =======================================
def get_amount_of_word(received_file, words_amount = 0, target_word = input("Enter word which amount you wont find: ")) -> int:
    words = HW3.get_all_words_from_file(received_file = received_file)
    for value in words:
        if target_word == value:
            words_amount += 1
    return words_amount
#======================================= Task #6 =======================================
def replace_word(received_file, target_word = input("Enter word you want replace: "), replace_word = input("Enter word on which you want replace target word:")) -> None:
    line_with_word_index = 0
    lines = open(received_file).readlines()
    for index, value in enumerate(lines):
        if target_word in value:
            line_with_word_index = index
            break
    lines[line_with_word_index].replace(target_word, replace_word)



files = HW3.get_files()
# Task #1
compare_lines_of_files(file_1=files[0], file_2=files[1])
# Task #2
make_file_with_params(received_file=files[0]) 
# Task #3
delete_last_line(received_file=files[0])
# Task #4
print(f"Length of longest line in file: {get_longest_line_length(received_file=files[1])}")
# Task #5
print(f"Amount of selected words in file: {get_amount_of_word(received_file=files[0])}")
# Task #6
replace_word(received_file=files[1])