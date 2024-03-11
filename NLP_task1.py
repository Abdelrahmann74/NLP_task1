import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = input("Enter a text: ")

choice = input("Choose one of the following options:\n1. Print tokenized words\n2. Print tokenized sentences\n3. Print output using split function\nChoice: ")

if choice == '1':
    tokens = word_tokenize(text)
    print("Tokenized words:", tokens)
elif choice == '2':
    sentences = sent_tokenize(text)
    print("Tokenized sentences:", sentences)
elif choice == '3':
    words = text.split()
    print("Output using split function:", words)
else:
    print("Invalid choice. Please choose a valid option.")