mainMenu = True
createUsers = False
while mainMenu:
    print("HACER ALGO CHULO TIPO PROFE!!!!!!!!!!!!!!!!!!!!!!!!")
    print("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit")
    print("")
    opt = input("Option: ")
    if not opt.isdigit():
        print("=" * 4 + "Invalid option"+"="*4+"\n")
    elif int(opt)<1 or int(opt)>5:
        print("="*4+"Invalid option"+"="*4+"\n")
    elif opt == "2":
        createUsers = True
        mainMenu = False
        while createUsers:
            print("")
            while True:
                username = input("Username: ")
                if len(username) < 5 or len(username) > 10:
                    print("Length of username have to be longer than 5 and shorter than 11")
                elif username.isalnum() is False:
                    print("They can only be alphanumeric characters")
                else:
                    break
            while True:
                password = input("Password: ")
                length = False
                if len(password) < 8 or len(password) > 12:
                    length = False
                else:
                    length = True
                upper = False
                lower = False
                digit = False
                not_Alfa = False
                spaces = False
                for i in password:
                    if i.islower() is True:
                        lower = True
                    if i.isupper() is True:
                        upper = True
                    if i.isdigit() is True:
                        digit = True
                    if i.isalnum() is False:
                        not_Alfa = True
                    if i.isspace() is True:
                        spaces = True
                        break
                if length == True and upper==True and lower==True and digit==True and not_Alfa==True and spaces==False:
                    print("USER CREATED")
                    print("")
                    input("Enter to continue")
                    print("")
                    createUsers = False
                    mainMenu = True
                    break
                elif length == False:
                    print("Length of password is not correct")
                elif not_Alfa == False:
                    print("Password has to contain some especial character")
                elif spaces == True:
                    print("Password cannot contain spaces")
                elif digit == False:
                    print("Password has to contain some digit")
                elif lower == False or upper == False:
                    print("Password have to include some uppercase and some lowercase")









