import sys


NUMBER_OF_LETTERS_IN_HAND = 7

scores = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
          "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def get_letter_score(letter_tile):
    return scores[letter_tile.lower()]

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

# starting_rack = "Xlwrpyu".upper()    # TODO: Input from the command line when you manually run the program

starting_rack = input("Enter the letters on your rack: ").upper()
if len(starting_rack) != NUMBER_OF_LETTERS_IN_HAND:
    print(f"You have an invalid hand containing {len(starting_rack)} letters!")
    sys.exit(1)

words = []
# Read in the words from the text file
with open('./sowpods.txt', 'r') as wordlist:
    all_words = wordlist.read().split()
    # Now remove all words that are too long
    for word in all_words:
        if len(word) <= NUMBER_OF_LETTERS_IN_HAND:
            words.append(word)

if not words:
    print("No words in your word list!")
    sys.exit(2)

saved_words = []
results = {}
for word in words:
    # Keep a temporary rack for each word checked
    check_rack = starting_rack

    keep_word = True
    for letter in word:
        letter_matched = check_rack.find(letter)
        if letter_matched >= 0:
            # Remove letter from temporary rack
            check_rack = check_rack[:letter_matched] + check_rack[letter_matched + 1:]
        else:
            # Letter not found so skip this word
            keep_word = False
            break

    if keep_word:
        saved_words.append(word)

if not saved_words:
    print(f"There are not matching words for your letters: {starting_rack}")

for word in saved_words:
    score = 0
    for letter in word:
        score += get_letter_score(letter)

    # Store the scores in a dictionary
    results[word] = score

# Sort the results - highest score first
sorted_dict_desc = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

print(f"The letters in your rack ({starting_rack}) can make {len(sorted_dict_desc)} words.\n"
      f"Here they are with their corresponding scores:")
for word in sorted_dict_desc:
    print(f"{word} = {sorted_dict_desc[word]}")
