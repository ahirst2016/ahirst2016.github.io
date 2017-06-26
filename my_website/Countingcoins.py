'''Coin Counter

Description:  This program converts the amount of money input by
                the user into the equivalent amount using the
                fewest coins possible(quarters, dimes, nickles, and pennies)

by Aaron Hirst

6/25/2017'''

quarters = 0
dimes = 0
nickles = 0
pennies = 0

def countcoins():
    amount = input("Please enter the number of dollars")
    amount = amount*100

    global quarters
    global dimes
    global nickles
    global pennies

    while amount >= 25:
        amount = amount - 25
        quarters = quarters +1

    while amount >= 10:
        amount = amount - 10
        dimes = dimes +1

    while amount >= 5:
        amount = amount - 5
        nickles = nickles +1

    while amount >= 1:
        amount = amount - 1
        pennies = pennies + 1

    print "There are "
    print quarters, " quarters"
    print dimes, " dimes"
    print nickles, " nickles"
    print pennies, " pennies"
