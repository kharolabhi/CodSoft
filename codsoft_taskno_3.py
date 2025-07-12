import random
import array
print("""/
                             _                               _             
                            | |                             | |            
 _ __   __ _ _____      ____| |    __ _  ___ _ __  _ __ __ _| |_ ___  _ __ 
| '_ \ / _` / __\ \ /\ / / _` |   / _` |/ _ \ '_ \| '__/ _` | __/ _ \| '__|
| |_) | (_| \__ \\ V  V / (_| |  | (_| |  __/ | | | | | (_| | || (_) | |   
| .__/ \__,_|___/ \_/\_/ \__,_|   \__, |\___|_| |_|_|  \__,_|\__\___/|_|   
| |                         ______ __/ |                                   
|_|                        |______|___/                                    
                                                                   --- by jigyashu bhatt
                                                   
""")


MAX_LEN = int(input("Enter Maximum size of password"))


Dnums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lwr_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

upe_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbl = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


jumble_pass = Dnums + upe_char + lwr_char + symbl


rand_digit = random.choice(Dnums)
rand_upper = random.choice(upe_char)
rand_lower = random.choice(lwr_char)
rand_symbol = random.choice(symbl)


temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(jumble_pass)


    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)


password = ""
for x in temp_pass_list:
    password = password + x


print(password)
