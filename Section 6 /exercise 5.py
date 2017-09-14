'''
Here's a rather challenging exercise that integrates functions, loops,
conditionals, and file handling.

In exercise 4, you recursively printed out converted temperature in the
command line. For this exercise, please consider the same list of Celsius
values again as input:

temperatures=[10,-20,-289,100]

Try to make a script that converts Celsius to Fahrenheit and
creates a text file and stores the converted values inside the text file.
Your text file content should look like this:

50.0
-4.0
212.0

Please don't write any message in the text file when input is lower than
-273.15.

'''

def cel_to_fah(cel):

    return((cel*9/5)+32)

temperatures=[10,-20,-289,100]

for temp in temperatures:

    if temp < -273.15:

        pass

    else:

        with open('temperature.txt', 'r+') as file:

            file.read()

            file.write(str(cel_to_fah(temp))+ '\n')
