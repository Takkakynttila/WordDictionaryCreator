from functions import data_bank

def main():
    # promt the user for parameters
    length = input('Give desired word length (0 <= n <= 8): ')
    if int(length) > 8:
        print('Invalid')
        quit()
    char_set = input('Choose character set: \n'
    + '[1] ASCII\n'
    + '[2] Lower case alphabet \n'
    + '[3] Test set \n>>> ')

    #initialize an object based on parameters
    f = data_bank(length, char_set)

    # flex with some calculations
    print('Amount of permutations: ' + str(f.calculate_combinations()))
    print('Approx filesize: \n'
    + '[+]' + str(f.calculate_size_approximation()) + ' bytes \n'
    + '[+]' + str(f.calculate_size_approximation() / 1000000) + ' megabytes')
    response = input('Create strings? y/n \n>>> ')

    if response.lower() == 'y':
        f.get_combinations(length)
    else:
        print('Aborting creation')
if __name__ == '__main__':
    main()


