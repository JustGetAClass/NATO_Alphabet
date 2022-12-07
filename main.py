# # Looping through dictionaries:
# for (key, value) in student_dict.items():
# #Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for(index, row) in nato_data.iterrows()}


def generate_phonetic():
    word = input("Enter a word ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only letters from the alphabet please")
        generate_phonetic()
    else:
        print(nato_word)


generate_phonetic()
