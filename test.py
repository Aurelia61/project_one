
letter_code = ""
number_code = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
coded_message = ""



number_code = int(input("Saisissez le number_code :"))
while number_code > 26:
    number_code -= 26
original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
coded_message = []
original_message = original_message.split()
for word in original_message:
    liste_word = []
    for letter in word:
        if letter == ".":
            liste_word.append(".")
        else :
            i = alphabet.index(letter)
            if i + number_code > 25:
                i -= 26
            liste_word.append(alphabet[i+number_code])
    coded_message.append("".join(liste_word))
print(" ".join(coded_message))

