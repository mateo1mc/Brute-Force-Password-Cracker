from random import randint
import os
import time

your_password = input("Enter a password: ")
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

start_time = time.time()
mached_password = ''
for idx, char in enumerate(your_password):
    found = False
    while not found:
        guess_index = randint(0, len(characters) - 1)
        if characters[guess_index] == char:
            mached_password += char
            found = True
            print("Found character:", char)
        print("Trying:", mached_password)
        print('Cracking Password ... Please Wait!')
        os.system('cls')  # clearing the screen, Windows --/-- Linux/MacOS --> os.system('clear')
end_time = time.time()

print('Your Password is: ', mached_password)
print("Time taken:", "{:.2f}".format(end_time - start_time), "seconds")
# code by @mateo1mc GitHub: https://github.com/mateo1mc
