#!/usr/#!/usr/bin/python3
#Have a string with each letter of the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Get user input if they want to decrpyt or encrypt a word
answer = input("Would you like to encrypt or decrypt a word? ('e' for \n"
               "encrypt, 'd' for decrypt): ").lower()
#create a while loop until they decide to encrypt or decrypt
while answer != "e" or "d":
#ask for word, make it uppercase to match the alphabet
    if answer == "e":
        word = input("What is the word to encrypt? ").upper()
#ask by how many letters in the alphabet they want the word rotated
        rotation = int(input("How would you like to have the alphabet rotated?\n"
                             "(3 would be for Caesar Cipher!): "))
#create empty strings and we will add encrypted letters to them
        cryptletter = ""
        crpytword = ""
#we will take each letter in the word they gave us, add their rotation to their index (using
# the find function), and then take that number and find the
#modulus when that number is divided by 26 to find the encrypted letter
        for letter in word:
            cryptletter = alphabet[(alphabet.find(letter) + rotation) % 26]
#if there is a space in the word/phrase they give us, this function will add a space to the encryption
            if letter == " ":
                cryptletter = " "
#combine the crypt letters to form the new word
            crpytword += cryptletter
#present the word(or words) and end the loop
        print(f"{word} encrypted by {rotation} is {crpytword}")
        break
    elif answer == "d":
#have them find a word they want to decrypt, and make it upper case to match the alphabet string
        word = input("What is the word to decrypt? ").upper()
#Ask them for their decryption method
        rotation = int(input("How were the letters rotated?: "))
#create two empty strings we will add letters once they go through the for loop
        cryptletter = ""
        cryptword = ""
#find the index of the letter in the alphabet, subract its rotation ,and find the modulus
#of that number divided by 26 to get the new letter
        for letter in word:
            cryptletter = alphabet[(alphabet.find(letter) - rotation) % 26]
            if letter == " ":
                cryptletter = " "
#add the letters together to make the cryptword, print the old and new words, and break the loop
            cryptword += cryptletter
        print(f"{word} decrypted by {rotation} is {cryptword}")
        break
#This loop will keep asking them to answer e or d to encrypt/decrypt a word
    else:
        answer = input("Would you like to encrypt or decrypt a word? ('e' for \n"
                       "encrypt, 'd' for decrypt): ").lower()