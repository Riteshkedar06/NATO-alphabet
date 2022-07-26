student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(new_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word").upper()
result = [new_dict[letter] for letter in user_input]
print(result)
