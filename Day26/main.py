import pandas as pd

phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame
phonetic_dict = {row.letter: row.code for index, row in phonetic_df.iterrows()}

# Get a word from the user
while True:
    try:
        word = input("Enter a word: ").upper()

    # Create a list of phonetic code words for each letter in the word
        phonetic_code_words = [phonetic_dict[letter] for letter in word ]

    # Print the resulting list
        print(phonetic_code_words)
        break

    except KeyError:
        print("Sorry, only letters in the alphabet please.")


