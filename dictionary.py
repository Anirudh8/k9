print('WELCOME TO WORD FINDER IN DICTIONARY')
aa=input('Enter the alphabets to search:')
searchfile = open("words_alpha.txt")
for line in searchfile:
    if aa in line: print(line)
searchfile.close()
