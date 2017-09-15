'''
Here is a tricky exercise.

Please download the ZIP file in the Resources and unzip it in a folder.

Then create a script that merges the three text files into a new text
file containing the text of all three files. The filename of the merged
text file should contain the current timestamp down to the millisecond level.
E.g. "2016-06-01-13-57-39-170965.txt".

You have some tips in the next lecture and the solution in the lecture after
that.
'''

import datetime

content = []

files = ['file1.txt','file2.txt','file3.txt']

for item in files:

    with open(item, 'r') as file:

        content.append(file.read())

filename = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f') + '.txt'

with open(filename, 'w') as file:

    for i in content:

        file.write(i + '\n')

        

