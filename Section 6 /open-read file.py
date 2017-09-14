file = open('example.txt','r')

content = file.read() #content type string

print(content)

file.seek(0) #Returns pointer position to begining of the file

content2 = file.readlines() #Saves file content in a list

content2 = [i.rstrip("\n") for i in content2] #Cleans up the list - strips the \n characters

print(content2)

file.close()
