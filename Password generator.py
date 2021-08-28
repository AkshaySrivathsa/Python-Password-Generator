"""---------------Password generator---------------"""

import random
while True:
    print('\n      ---------------Phoenix Password Generator---------------')
    print('---------------Welcome to the best password generator---------------\n')
    print('1. Generate Password     (type 1)')
    print('2. exit                  (type 2)')
    try:
        option = int(input('enter the option: '))
        if option == 1:
            length = int(input('enter the length of the password: '))
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}-_=+><'
            char_list = []
            for i in characters:
                char_list.append(i)
            print('The randomly generated password is: ')
            for i in range(length):
                print(random.choice(char_list), end='')

        elif option == 2:
            quit()

    except Exception as e:
        print('please enter a valid option(integers only)')
