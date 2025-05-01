#Take user input
sentence = input("Enter your sentence:")

#print out letters
print("\n Letters:")
for letter in sentence:
    print(letter.upper())

#print out words
print("\n Words:")
words = sentence.split()
for word in words:
    print(word[0].upper() + word[1:])
    
