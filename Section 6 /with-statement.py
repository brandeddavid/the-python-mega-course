with open ('example1.txt', 'r+') as file:

    file.seek(0)

    content = file.read()

    toAppend = ['Append 1','Append 2','Append 3']

    for item in toAppend:

        file.write('\n' + item)
