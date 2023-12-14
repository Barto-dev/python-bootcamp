import pandas

alphabet_data_raw = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(alphabet_data_raw)
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_translation = [phonetic_dict[letter] for letter in user_input]
print(phonetic_translation)
