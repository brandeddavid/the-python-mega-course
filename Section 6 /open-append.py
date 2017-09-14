file = open('example.txt', 'a')

toAppend = ['Appended 1','Appended 2','Appended 3','Appended 4','Appended 5']

for item in toAppend:

    file.write(item + "\n")


file.close()
