from functions import data_bank

def main():
    # promt the user for parameters
    length = input('Give desired word length: ')
    char_set = input('Choose character set: \n'
    + '[1] ASCII\n'
    + '[2] Lower case alphabet \n>>> ')

    #initialize an object based on parameters
    f = data_bank(length, char_set)

    # flex with some calculations
    print('Amount of permutations: ' + str(f.calculate_permutations()))
    print('Approx filesize: \n'
    + str(f.calculate_size_approximation()) + ' bytes \n'
    + str(f.calculate_size_approximation() / 1000000) + ' megabytes')
    response = input('Create strings? y/n \n>>> ')

    if response.lower() == 'y':
        x = 0
        word_as_list = [f.get_char(0)] * int(length)
        char_list = f.get_char_list()
        while x < int(length):
            for char in word_as_list:
                for char in char_list:
                    word_as_list[x] = char
                    print(str(word_as_list))
            x += 1
    else:
        print('Aborting creation!')
if __name__ == '__main__':
    main()
