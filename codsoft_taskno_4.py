
import random

print("""\
######                          ######                                  #####                                       
#     #  ####   ####  #    #    #     #   ##   #####  ###### #####     #     #  ####  #  ####   ####   ####  #####  
#     # #    # #    # #   #     #     #  #  #  #    # #      #    #    #       #    # # #      #      #    # #    # 
######  #    # #      ####      ######  #    # #    # #####  #    #     #####  #      #  ####   ####  #    # #    # 
#   #   #    # #      #  #      #       ###### #####  #      #####           # #      #      #      # #    # #####  
#    #  #    # #    # #   #     #       #    # #      #      #   #     #     # #    # # #    # #    # #    # #   #  
#     #  ####   ####  #    #    #       #    # #      ###### #    #     #####   ####  #  ####   ####   ####  #    #             
                                                                                                    --by jigyashu
                                                                                                                     """)
while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")



    usr_imp = int(input("Enter your choice :"))


    while usr_imp > 3 or usr_imp < 1:
        usr_imp = int(input('Enter a valid choice please '))


    if usr_imp == 1:
        usr_imp_name = 'Rock'
    elif usr_imp == 2:
        usr_imp_name = 'Paper'
    else:
        usr_imp_name = 'Scissors'


    print('User choice is \n', usr_imp_name)
    print('Now its Computers Turn....')


    comp_usr_imp = random.randint(1, 3)


    while comp_usr_imp == usr_imp:
        comp_usr_imp = random.randint(1, 3)


    if comp_usr_imp == 1:
        comp_usr_imp_name = 'RocK'
    elif comp_usr_imp == 2:
        comp_usr_imp_name = 'Paper'
    else:
        comp_usr_imp_name = 'Scissors'
    print("Computer choice is \n", comp_usr_imp_name)
    print(usr_imp_name, 'Vs', comp_usr_imp_name)

    if usr_imp == comp_usr_imp:
        print('Its a Draw', end="")
        result = "DRAW"

    if (usr_imp == 1 and comp_usr_imp == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (usr_imp == 2 and comp_usr_imp == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (usr_imp == 1 and comp_usr_imp == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (usr_imp == 3 and comp_usr_imp == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (usr_imp == 2 and comp_usr_imp == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (usr_imp == 3 and comp_usr_imp == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == usr_imp_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break

print("thanks for playing")
