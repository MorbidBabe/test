#!/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''
message = input('please enter a message:')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newposition = (position + key) % 26 
        newCharacter = alphabet [newposition]
        newMessage += newCharacter
    else:
        newMessage += character
print(newMessage)
