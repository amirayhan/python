# dictionary item
my_dict = {
    'Rayhan' : 29,
    'Aysha' : 13,
    'Pranto' : 90,
    'Sabbir' : 80,
    'Ilhan' : 95,
    'Alamgir' : 98,
    'Siraj' : 99,
    'Jahangir' : 100
}

# repeat again for oparation
while True:
    # show all oparations
    print('\nAll Oparation: ')
    print('==================')
    print(' 1. Add Name & Mark \n 2. Remove Name \n 3. Find Mark')

    # choose a oparation item
    choice = input('\nChoose your Oparation: ')

    # when choose a oparation item
    if choice in ('1','2','3'):
        
        #first try this
        try:
            # 1. Add Name & Mark
            if choice == '1':
                print(' 1. Add Name & Mark')
                name = input('Enter Name: ')
                mark = int(input('Enter Mark: '))
                my_dict[name] = mark
                print(f'\nSuccessfully Added! \n\n{my_dict}')

            #2. Remove Name
            elif choice == '2':
                print('2. Remove Name')
                name = input('Enter Name: ')
                if name in my_dict:
                    del my_dict[name]
                    print(f'\nSuccessfully Deleted! \n{my_dict}')
                else:
                    print('\nNot Found! Try Again.\n')

            # 3. Find Mark
            elif choice == '3':
                print('3. Find Mark')
                name = input('Enter Name: ')
                if name in my_dict:
                    print(f'\nCongratulations! \nMark is: {my_dict[name]}')
                else:
                    print('\nNot Found! Try Again.\n')

            # if want to new oparation again
            next_oparation = input('\nDo you want to try oparation again(y/n): ')
            
            if next_oparation.lower() != 'y':
                print('\n\nThank you for your Time!\n\n')
                break
        
        # if try not work
        except ValueError:
            print('Please Enter Valid Input')
    
    else:
        print('\nInvalid Choice! Please select 1, 2, or 3.')

        
    
    




