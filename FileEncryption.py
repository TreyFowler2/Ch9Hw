from base64 import encode
import csv

infile = open('info_security.txt', 'r')
infile.data = infile.read()
totalwords = infile.data.strip()
outfile = open('encrypted.txt', 'w')

#define dictionary
alphabet_list = {'A':'@', 'a':')', 'B':'S', 'b':'#', 'C':'.', 'c':'>', 
'D':'~', 'd':'<', 'E':'^', 'e':':', 'F':']', 'f':'$', 'G':'%', 'g':'?', 
'H':'M', 'h':'X', 'I':'*', 'i':';', 'J':'!', 'j':'|', 'K':'&', 'k':'B',
'L':'`', 'l':'(', 'M':'T', 'm':'W', 'N':'V', 'n':'[', 'O':'-', 'o':'_', 
'P':'+', 'p':'=', 'Q':'a', 'q':'n', 'R':'c', 'r':'C', 'S':'q', 's':'m', 
'T':'t', 't':'T', 'U':'f', 'u':'3', 'V':'7', 'v':'1', 'W':'0', 'w':'2', 
'X':'5', 'x':'4', 'Y':'j', 'y':'i', 'Z':'z', 'z':'f'}

#provide empty message
codedmessage = ""

#for loop to iterate through each letter
for letter in totalwords:

    #if statement to iterate through each key to assign encrypted value
    if letter in alphabet_list:
        codedmessage = codedmessage + alphabet_list[letter]
    else:
        codedmessage = codedmessage + letter

outfile.write(str(codedmessage))




