# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)


longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

longest = max(longest_german_word,longest_hungarian_word,longest_finnish_word,strong_password)      #max is a string operation to identify the string with maximum characters

# Now that you know what the longest word is, print it out in an f-string below

print(f"The longest string is {longest}, containing {len(longest)} characters.")        #final output
