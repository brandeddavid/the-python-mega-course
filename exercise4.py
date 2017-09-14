def cel_to_fah(cel):

    return((cel*9/5)+32)

temperatures=[10,-20,-289,100]

for temp in temperatures:

    if temp < -273.15:

        print("That temperature doesn't make sense")

    else:

        print(cel_to_fah(temp))
