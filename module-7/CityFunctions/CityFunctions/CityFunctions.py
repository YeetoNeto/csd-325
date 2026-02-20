# Program that stores a function that accepts two paramters City, Country


def cityCountry(City, Country, Language='', population=''):
    if population == '' and Language == '':
        string = f'{City},{Country}'
    elif population == '':
        string = f'{City},{Country},{Language}'
    elif Language == '':
        string = f'{City},{Country},{population}'
    else:
        string = f'{City},{Country},{Language}, {population}'

    return string


def main():
    print('You live in ' + cityCountry('Santiago', 'Chile'))
    print('You live in ' + cityCountry('Virginia', 'United States', 50000))
    print('You live in ' + cityCountry('Tokyo', 'Japan', 'Japanese', 60000))
    

#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()