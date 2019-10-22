print("Lesson 4 - Strings\n") # prints a new line after the string
print("\"Print a quotation\"\n")
print("Print a \\\n")
word = "jawn"
print("Print the variable: " + word + "\n")
caps = "WE DONT LIKE BOULS WHO CAP"
print("Lower Case: " + caps.lower() + "\n")
low = "my Flow highkey"
print("Upper Case: " + low.upper() + "\n")
print(caps.isupper())
print("")
print(str(low.islower()) + " because \"F\" is upper case")  # Converts the Boolean to a string
print("")
print(low.upper().isupper())  # Chain Functions together
print("")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Print the first letter: " + alphabet[0])  # Strings are indexed like arrays
print("")
ind = alphabet.index("F") # Finds index of letter in argument
print(ind)
print(alphabet[ind])
print("")
mistake = "I misspelled chiken"
print(mistake)
print(mistake.replace("chiken", "chicken").replace("misspelled", "fixed"))
# Use Replace Function to replace parts of a string














