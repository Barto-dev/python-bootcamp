import pandas

alphabet_data_raw = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(alphabet_data_raw)
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_translation = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_translation)


generate_phonetic()
