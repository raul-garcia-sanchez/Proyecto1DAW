import pymysql
conn = pymysql.connect(host='40.118.88.187',user='raul',password='P@ssw0rd',db='CHOOSEYOURSTORY')

import Herramientas.funcionesAuxiliares as FA

main_menu = True
play_menu = False
reports_menu = False
replay_menu = False
username = ""
while main_menu:
    FA.main()
    textOpts = "\n1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit"
    inputOptText = "\nOption:\n"
    lista = ["1", "2", "3", "4","5"]
    opcion = FA.getOpt(textOpts, inputOptText, lista)
    if opcion == "1":
        isCorrectLogin = False
        while not isCorrectLogin:
            username = input("Username: ")
            password = input("Password: ")
            isCorrectLogin = FA.checkUserbdd(username, password)
            if not isCorrectLogin:
                print("Username or password are not correct")
        print(f"Hello {username}, lets play!!")
        print("What adventure do you want to play?\n\n")
        while True:
            adventures = FA.get_adventures_with_chars()
            print(FA.getFormatedAdventures(adventures))
            id_adventure_choosen = input("\n\nWhat adventure do you want to play?(0 go back):\n")
            print("\n\n")
            if id_adventure_choosen == "+":
                print("SCROLL MORE")
            elif id_adventure_choosen == "-":
                print("SCROLL LESS")
            elif id_adventure_choosen == "0":
                break
            elif id_adventure_choosen.isdigit() == False:
                print("HAS TO BE AN INTEGER")
            elif int(id_adventure_choosen) not in adventures:
                print("ID AVENTURA DOESN'T EXIST")
            elif int(id_adventure_choosen) in adventures:
                adventure = adventures[int(id_adventure_choosen)]
                print(FA.getHeader(adventure['Name']))
                print(FA.getFormatedBodyColumns(("Adventure:", f"{adventure['Name']}"),(19,70),0))
                print(FA.getFormatedBodyColumns(("Description:", f"{adventure['Description']}"),(19,70),0))
                print("\n")
                while True:
                    header_characters = str("Characters").center(70, "=")
                    print(header_characters)
                    characters = FA.get_characters()
                    for i in adventure['characters']:
                        print(f"{i}) {characters[i]}")
                    id_character_choosen = input("\nSelect your Character (0 go back):\n")
                    if id_character_choosen.isdigit() == False:
                        print("HAS TO BE AN INTEGER")
                    elif int(id_character_choosen) in adventure['characters']:
                        print(f"You have selected play {characters[int(id_character_choosen)]}\n")
                        input("Enter to continue")
                        print("\n\n")
                        id_step = 1
                        desition_making = []
                        while True:
                            print(FA.getHeader(adventure['Name']))
                            steps = FA.get_id_bystep_adventure()
                            print(FA.formatText(steps[id_step]['Description'],100,"\n").replace("%personatge%",f"{characters[int(id_character_choosen)]}"))
                            if steps[id_step]['Final_Step'] == 0:
                                print("Options:\n")
                                id_and_option = FA.get_id_choice(id_step)
                                for i in id_and_option:
                                    print(FA.getFormatedBodyColumns(("",f"{i[0]})",f"{i[1]}".replace("%personaje%",f"{characters[int(id_character_choosen)]}")),(3,5,95),3))
                                while True:
                                    id_option_choosen = input("\n\nSelect Option:\n")
                                    if id_option_choosen.isdigit() == False:
                                        print("HAS TO BE AN INTEGER")
                                    else:
                                        break
                                answer = FA.get_id_answer(id_option_choosen)
                                is_correct = False
                                for i in id_and_option:
                                    if i[0] == int(id_option_choosen):
                                        desition_making.append((int(id_option_choosen), id_step))
                                        id_step = i[3]
                                        is_correct = True
                                        break
                                if not is_correct:
                                    print("INVALID OPTION")
                                else:
                                    for i in answer:
                                        print(FA.formatText(i[1],100,"\n"))
                                    input("\nEnter to continue")
                                    print("\n")
                            else:
                                print("\n")
                                FA.final()
                                desition_making.append((int(id_option_choosen), id_step))
                                input("\n\nEnter to continue")
                                id_user = FA.getIdUser(username)
                                id_personage = id_character_choosen
                                id_adventure = id_adventure_choosen
                                FA.insertCurrentGame(id_user, id_personage, id_adventure)
                                for i in desition_making:
                                    FA.insert_decisions(i[0],FA.identificador_game(),i[1])
                                character_menu = False
                                break
                            main_menu = False
                            play_menu = True
                        break
                    elif id_character_choosen == "0":
                        break
                    elif int(id_character_choosen) not in adventure['characters']:
                        print("CHARACTER DOESN'T EXIST")
                break
    if opcion == "2":
        while True:
            username = input("Username: ")
            if FA.checkUser(username) == True and FA.userExists(username) == False:
                FA.checkUser(username)
                FA.userExists(username)
                while True:
                    password = input("Password: ")
                    if FA.checkPassword(password) == True:
                        FA.checkPassword(password)
                        FA.insertUser(username, password)
                        print("USER CREATED")
                        break
                break
        main_menu = False
        play_menu = True
    if opcion == "3":
        print("\n")
        FA.title_adventure()
        input("Enter to continue")
        main_menu = False
        replay_menu = True
        while replay_menu:
            print(FA.header_replay_adventures())
            print("")
            games_played = FA.games()
            list_games_played = []
            for i in games_played:
                print(f"{str(i[0]).ljust(14)} {str(i[1]).ljust(19)} {str(i[2]).ljust(27)} {str(i[3]).ljust(19)} {i[4]}")
                list_games_played.append(i[0])
            print("")
            while True:
                id_adventure_choosen = input("\n\nWhat adventure do you want to play?(0 go back):\n")
                if id_adventure_choosen.isdigit() == False:
                    print("HAS TO BE AN INTEGER")
                elif int(id_adventure_choosen) in list_games_played:
                    print(f"You have selected the game {id_adventure_choosen}")
                    print("\n")
                    break
                elif id_adventure_choosen == "0":
                    replay_menu = False
                    main_menu = True
                    break
                else:
                    print("ADVENTURE DOESN'T EXIST")
            steps = FA.get_id_bystep_adventure()
            while True:
                for i in FA.option_replay(id_adventure_choosen):
                    id_actual_step = i[1]
                    print(FA.getHeader(FA.name_adventure(id_adventure_choosen)))
                    character = FA.name_character(id_adventure_choosen)
                    for k in character:
                        name_character_game = k[0]
                    print(FA.formatText(steps[id_actual_step]['Description'], 100, "\n").replace("%personatge%", name_character_game))
                    if steps[id_actual_step]['Final_Step'] == 0:
                        print("Options:\n")
                        id_and_option = FA.get_id_choice(id_actual_step)
                        for j in id_and_option:
                            print(FA.getFormatedBodyColumns(("", f"{j[0]})", f"{j[1]}".replace("%personaje%",name_character_game)), (3, 5, 95), 3))
                        input("\nEnter to continue:")
                        print("")
                        print(f"Option {i[0]} selected")
                        answer = FA.get_id_answer(str(i[0]))
                        print(FA.formatText(answer[0][1],100,"\n"))
                    input("\nEnter to continue:")
                    print("")
                if id_adventure_choosen == "0":
                    break
                else:
                    FA.final()
                    input("\nEnter to continue:")
                    print("")
                    break
    if opcion == "4":
        main_menu = False
        reports_menu = True
        while reports_menu == True:
            print("\n")
            FA.reports()
            textOpts = "\n1)Most used answer\n2)Player with more games played\n3)Games played by user\n4)Back"
            inputOptText = "\nOption:\n"
            lista = ["1", "2", "3", "4"]
            opcion = FA.getOpt(textOpts, inputOptText, lista)
            if opcion == "1":
                print(FA.getHeaderAnswers("ID AVENTURA - NOMBRE".ljust(30) +"ID PASO - DESCRIPCION".ljust(30) + "ID RESPUESTA - DESCRIPCION".ljust(30) + "NUMERO VECES SELECCIONADA","Most used answer"))
                answers = FA.answer_more_used()
                result = ""
                for i in answers:
                    print(FA.getFormatedBodyColumns((str(i[0]),str(i[1]),str(i[2]),str(i[3])),(30,30,30,30),5))
                input("Enter to continue")
            if opcion == "2":
                print("")
                print(FA.getHeaderAnswers("NOMBRE USUARIO".ljust(60) + "PARTIDAS JUGADAS".ljust(70),"Player with more games played"))
                more_games_played = FA.player_more_games()
                for i in more_games_played:
                    print(f"{str(i[0]).ljust(59)} {i[1]}")
                input("\n\nEnter to continue")
            if opcion == "3":
                while True:
                    username = input("What user do you want to see?\n")
                    if FA.userExists(username) == False:
                        print("User not created")
                    else:
                        break
                print(FA.getHeaderAnswers("IdAdventure".ljust(33) + "Name".ljust(45) + "Date".ljust(30),f"Games played by {username}"))
                games_user = FA.games_played_user(username)
                for i in games_user:
                    print(f"{str(i[0]).ljust(32)} {str(i[1]).ljust(44)} {i[2]} \n")
                input("\n\nEnter to continue")
            if opcion == "4":
                play_menu = False
                reports_menu = False
                main_menu = True
    if opcion == "5":
        break
    while play_menu == True:
        FA.main()
        textOpts = "\n1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Exit"
        inputOptText = "\nElige tu opción:"
        lista = ["1", "2", "3", "4","5"]
        opcion = FA.getOpt(textOpts, inputOptText, lista)
        if opcion == "1":
            print(f"Chao {username}, hope you come back soon\n")
            input("\nEnter to continue")
            play_menu = False
            reports_menu = False
            replay_menu = False
            main_menu = True
        if opcion == "2":
            print("\n\n")
            while True:
                adventures = FA.get_adventures_with_chars()
                print(FA.getFormatedAdventures(adventures))
                id_adventure_choosen = input("\n\nWhat adventure do you want to play?(0 go back):\n")
                print("\n\n")
                if id_adventure_choosen == "+":
                    print("SCROLL MORE")
                elif id_adventure_choosen == "-":
                    print("SCROLL LESS")
                elif id_adventure_choosen == "0":
                    break
                elif id_adventure_choosen.isdigit() == False:
                    print("HAS TO BE AN INTEGER")
                elif int(id_adventure_choosen) not in adventures:
                    print("ID AVENTURA DOESN'T EXIST")
                elif int(id_adventure_choosen) in adventures:
                    adventure = adventures[int(id_adventure_choosen)]
                    print(FA.getHeader(adventure['Name']))
                    print(FA.getFormatedBodyColumns(("Adventure:", f"{adventure['Name']}"), (19, 70), 0))
                    print(FA.getFormatedBodyColumns(("Description:", f"{adventure['Description']}"), (19, 70), 0))
                    print("\n")
                    while True:
                        header_characters = str("Characters").center(70, "=")
                        print(header_characters)
                        characters = FA.get_characters()
                        for i in adventure['characters']:
                            print(f"{i}) {characters[i]}")
                        id_character_choosen = input("\nSelect your Character (0 go back):\n")
                        if id_character_choosen.isdigit() == False:
                            print("HAS TO BE AN INTEGER")
                        elif int(id_character_choosen) in adventure['characters']:
                            print(f"You have selected play {characters[int(id_character_choosen)]}\n")
                            input("Enter to continue")
                            print("\n\n")
                            id_step = 1
                            desition_making = []
                            while True:
                                print(FA.getHeader(adventure['Name']))
                                steps = FA.get_id_bystep_adventure()
                                print(FA.formatText(steps[id_step]['Description'], 100, "\n").replace("%personatge%", f"{characters[int(id_character_choosen)]}"))
                                if steps[id_step]['Final_Step'] == 0:
                                    print("Options:\n")
                                    id_and_option = FA.get_id_choice(id_step)
                                    for i in id_and_option:
                                        print(FA.getFormatedBodyColumns(("", f"{i[0]})", f"{i[1]}".replace("%personaje%", f"{characters[int(id_character_choosen)]}")),  (3, 5, 95), 3))
                                    while True:
                                        id_option_choosen = input("\n\nSelect Option:\n")
                                        if id_option_choosen.isdigit() == False:
                                            print("HAS TO BE AN INTEGER")
                                        else:
                                            break
                                    answer = FA.get_id_answer(id_option_choosen)
                                    is_correct = False
                                    for i in id_and_option:
                                        if i[0] == int(id_option_choosen):
                                            desition_making.append((int(id_option_choosen), id_step))
                                            id_step = i[3]
                                            is_correct = True
                                            break
                                    if not is_correct:
                                        print("INVALID OPTION")
                                    else:
                                        for i in answer:
                                            print(FA.formatText(i[1], 100, "\n"))
                                        input("\nEnter to continue")
                                        print("\n")
                                else:
                                    print("\n")
                                    FA.final()
                                    desition_making.append((int(id_option_choosen), id_step))
                                    input("\n\nEnter to continue")
                                    id_user = FA.getIdUser(username)
                                    id_personage = id_character_choosen
                                    id_adventure = id_adventure_choosen
                                    FA.insertCurrentGame(id_user, id_personage, id_adventure)
                                    for i in desition_making:
                                        FA.insert_decisions(i[0], FA.identificador_game(), i[1])
                                    character_menu = False
                                    break
                                main_menu = False
                                play_menu = True
                            break
                        elif id_character_choosen == "0":
                            break
                        elif int(id_character_choosen) not in adventure['characters']:
                            print("CHARACTER DOESN'T EXIST")
                    break
        if opcion == "3":
            print("\n")
            FA.title_adventure()
            input("Enter to continue")
            main_menu = False
            replay_menu = True
            while replay_menu:
                print(FA.header_replay_adventures())
                print("")
                games_played = FA.games()
                list_games_played = []
                for i in games_played:
                    print(f"{str(i[0]).ljust(14)} {str(i[1]).ljust(19)} {str(i[2]).ljust(27)} {str(i[3]).ljust(19)} {i[4]}")
                    list_games_played.append(i[0])
                print("")
                while True:
                    id_adventure_choosen = input("\n\nWhat adventure do you want to play?(0 go back):\n")
                    if id_adventure_choosen.isdigit() == False:
                        print("HAS TO BE AN INTEGER")
                    elif int(id_adventure_choosen) in list_games_played:
                        print(f"You have selected the game {id_adventure_choosen}")
                        print("\n")
                        break
                    elif id_adventure_choosen == "0":
                        replay_menu = False
                        main_menu = True
                        break
                    else:
                        print("ADVENTURE DOESN'T EXIST")
                steps = FA.get_id_bystep_adventure()
                while True:
                    for i in FA.option_replay(id_adventure_choosen):
                        id_actual_step = i[1]
                        print(FA.getHeader(FA.name_adventure(id_adventure_choosen)))
                        character = FA.name_character(id_adventure_choosen)
                        for k in character:
                            name_character_game = k[0]
                        print(FA.formatText(steps[id_actual_step]['Description'], 100, "\n").replace("%personatge%",name_character_game))
                        if steps[id_actual_step]['Final_Step'] == 0:
                            print("Options:\n")
                            id_and_option = FA.get_id_choice(id_actual_step)
                            for j in id_and_option:
                                print(FA.getFormatedBodyColumns(("", f"{j[0]})", f"{j[1]}".replace("%personaje%", name_character_game)), (3, 5, 95), 3))
                            input("\nEnter to continue:")
                            print("")
                            print(f"Option {i[0]} selected")
                            answer = FA.get_id_answer(str(i[0]))
                            print(FA.formatText(answer[0][1], 100, "\n"))
                        input("\nEnter to continue:")
                        print("")
                    if id_adventure_choosen == "0":
                        break
                    else:
                        FA.final()
                        input("\nEnter to continue:")
                        print("")
                        break
        if opcion == "4":
            play_menu = False
            reports_menu = True
            while reports_menu == True:
                print("\n")
                FA.reports()
                textOpts = "\n1)Most used answer\n2)Player with more games played\n3)Games played by user\n4)Back"
                inputOptText = "\nOption:\n"
                lista = ["1", "2", "3", "4"]
                opcion = FA.getOpt(textOpts, inputOptText, lista)
                if opcion == "1":
                    print(FA.getHeaderAnswers("ID AVENTURA - NOMBRE".ljust(30) + "ID PASO - DESCRIPCION".ljust(30) + "ID RESPUESTA - DESCRIPCION".ljust(30) + "NUMERO VECES SELECCIONADA", "Most used answer"))
                    answers = FA.answer_more_used()
                    result = ""
                    for i in answers:
                        print(FA.getFormatedBodyColumns((str(i[0]), str(i[1]), str(i[2]), str(i[3])), (30, 30, 30, 30), 5))
                    input("Enter to continue")
                if opcion == "2":
                    print("")
                    print(FA.getHeaderAnswers("NOMBRE USUARIO".ljust(60) + "PARTIDAS JUGADAS".ljust(70), "Player with more games played"))
                    more_games_played = FA.player_more_games()
                    for i in more_games_played:
                        print(f"{str(i[0]).ljust(59)} {i[1]}")
                    input("\n\nEnter to continue")
                if opcion == "3":
                    while True:
                        username = input("What user do you want to see?\n")
                        if FA.userExists(username) == False:
                            print("User not created")
                        else:
                            break
                    print(FA.getHeaderAnswers("IdAdventure".ljust(33) + "Name".ljust(45) + "Date".ljust(30), f"Games played by {username}"))
                    games_user = FA.games_played_user(username)
                    for i in games_user:
                        print(f"{str(i[0]).ljust(32)} {str(i[1]).ljust(44)} {i[2]} \n")
                    input("\n\nEnter to continue")
                if opcion == "4":
                    reports_menu = False
                    play_menu = True
        if opcion == "5":
            main_menu = True
            play_menu = False
