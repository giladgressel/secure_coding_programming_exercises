# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
        #im not sure if theres some method other than string slicing
def check_pdf(f):
    if f[-3:] == "pdf":
        print(f,"is a pdf file.")
    else:
        print(f,"is not a pdf file.")          #defined the function to check the file extension

check_pdf(file_1)           #calling the function with each file
check_pdf(file_2)
check_pdf(file_3)
check_pdf(file_4)