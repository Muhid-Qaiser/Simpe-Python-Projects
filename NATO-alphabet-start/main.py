# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(nato_dict)


def nato_converter():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_converter()
    else:
        print(nato_list)


nato_converter()
