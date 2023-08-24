# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

sentence = word[1:3] + word[-1] + word[-2] + word[2:4] + word[-1] + word[0] + word[-3] + word[2:4] + word[-2]
print(sentence)