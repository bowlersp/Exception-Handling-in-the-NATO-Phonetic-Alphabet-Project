import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
  word = input(f"Please enter a word to translate to phonetic code\n").upper()
  try:
    phonetic_word = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, only letters in the alphabet")
    generate_phonetic()
  else:
    print(phonetic_word)

generate_phonetic()
