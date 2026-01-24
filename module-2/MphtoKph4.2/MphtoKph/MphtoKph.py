# Noah McCarthy, 10/23/2025, Module 4.2 Assignment
# The purpose of this program is to create a function that converts Miles to Kilometers

#Main function
def main():
    print('Hello, Welcome to MPH to KPH converter.')
    Continue = True

    #Loop to allow repetitive use
    while (Continue == True):
        #Try/except to catch any strings entered
        try:
          mph = float(input('\nHow many miles driven? '))
          #if statements to check 
          if (mph < 0):
              print('Numbers can not be negative. Please enter a valid number.')
              continue
          #Access the function to convert
          kph = MphtoKph(mph)
          print(f'The amount of miles entered was {mph:.2f} miles and that amount in kilometers is {kph:.2f} Kilometers.')

        except(ValueError):      
            print('It appears an error has occured, Please try using a valid number.')
            continue

        # Ask question to continue or not
        response = input('Enter "Y" to Continue, otherwise press enter to exit. ')
        if response != 'Y':
            Continue = False #Exits loop and ends program

    #Converter function
def MphtoKph(mph):
    convertNumber = 1.609
    return mph * convertNumber #return calcualtion to assign kph

#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()
