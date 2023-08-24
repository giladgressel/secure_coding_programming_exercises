# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
w1 = s[s.find("butter"):s.find("cups")]
print(w1)

w3 = s[s.find("flour"):s.find("ish")]
print(w3)

w4 = s[s.find("egg"):s.find("ins befo")]
print(w4)

w5 = s[s.find("apple"):s.find("d with")]
print(w5)