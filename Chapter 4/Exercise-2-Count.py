import re
word = "Hello my name is Amster Sani"  
filename = "sentence.txt"

with open(filename, 'r') as file_handler:
    for count, sentence in enumerate(file_handler):
        pass
    print('Total Lines', count + 1)
    for sentence in file_handler:
            if(sentence==word):
                count=count+1
    print("Repetition of the word", word, ":", count)