def cel_to_fah(cel):

    return((cel*9/5)+32)

temp = float(input('>'))

if temp < -273.15:

    print('Error')

else:

    print(cel_to_fah(temp))
