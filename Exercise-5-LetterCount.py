import string
file = open("sentences.txt", 'r') 
text = file.read() 
countletter = {} 
for letter in text:
    if letter in string.ascii_letters: 
        if letter in countletter:
            countletter[letter] += 1
        else:
            countletter[letter] = 1

for letter, letter_count in countletter.items(): 
    print(f'{letter}: {letter_count}')