#Noah McCarthy 1/18/26 Module 1.3
#The purpose of this code is to take an input of bottles and perform operations to take them off the wall till none remain

def main():

    #Error Checking
    try:
        Bottles = int(input("How many bottle's of beer are on the wall? "))

        #No point in playing if you dont have bottles or owe bottles
        if Bottles < 1:
            print("\nThere's no point of playing if you have less than a bottle of beer. It ruins the fun.\n")
            main() #call main for loop since it is only one simple line

    except ValueError: #Exception for when amount of bottles are not an int
        print('\nPlease inter a valid amount of bottles. You either have a full bottle or no bottle.\n')
        main() #Call main for loop since it is only one simple line

    BottlesOfBeer(Bottles) #Call the function that operates on the input


def BottlesOfBeer(Bottles):
    Loop = True
    while Loop == True:
        #While the amount isnt one state amount of bottles and remove one.
        if Bottles > 1:
            print(f'{Bottles} bottles of beer on the wall, {Bottles} bottles of beer.\n Take one down and pass it around, {Bottles-1} bottle(s) of beer on the wall. \n')
            Bottles -= 1        
        else: #When it is finish off the process
            print(f'{Bottles} bottle of beer on the wall, {Bottles} bottle of beer.\n Take one down and pass it around, {Bottles-1} bottle(s) of beer on the wall.\n\nTime to buy more bottles of beer.\n')
            Loop = False

#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()