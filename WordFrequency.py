infile = open('sometext.txt', 'r')

#checking total word count
infile.data = infile.read()
totalwords = infile.data.split()
#print(len(totalwords))

#creating empty dictionary to fill
word_dictionary = dict()

#counter to identifty words 
for word in totalwords:
    if word in word_dictionary:
        #word incrememter if there are multiple words
        word_dictionary[word] = word_dictionary[word] + 1
    else:
        #if no more words can be counted
        word_dictionary[word] = 1

print(word_dictionary, "WITH A TOTAL WORD COUNT OF:", len(totalwords))




