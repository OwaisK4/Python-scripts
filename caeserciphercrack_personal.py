#!/usr/bin/python
import sys
import string

def decrypt(letters,ciphertext,plaintext,key):
    #create a list from ciphertext to iterate over
    cipher_words = list(ciphertext)
    for i in range(len(cipher_words)):
        cipher_letter = cipher_words[i]
        for k in letters:
            #find out each letter by iterating to letters and also find index
            if cipher_letter == letters[k]:
                cipher_position = k
                #add key to index of each letter
                cipher_position += key
                #adjust out of bounds index
                cipher_position %= 26
                #convert the new index to letter and append to plaintext
                plaintext.append(letters[cipher_position])
    return plaintext
    #print("".join(plaintext))

letters = dict(enumerate(string.ascii_lowercase))
ciphertext = str(sys.argv[1]).lower()
plaintext = []
key = int(sys.argv[2])
print(decrypt(letters,ciphertext,plaintext,key))

#TODO Subsitute sys.argv with argparse
