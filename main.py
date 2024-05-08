import random

cont = 0

while True:
    print("\nVocê deseja jogar em qual língua? (EN/PT)")
    print("What language do you want to play? (EN/PT)")
    lang = input("Choose your language: ").upper()
    match lang:

        case "EN":
            while True:
                level = input("\nWhich level do you want to play? EASY (1-10) - MEDIUM (1-25) - HARD (1-50): ").upper()

                if level in ["EASY", "MEDIUM", "HARD"]:
                    break
                else:
                    print("Choose a difficulty")

            match level:
                case "EASY":
                    print("\nYou are on a number guessing game between 1 - 10 (1 and 10 included).\nGood luck!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    # while do jogo
                    while True:
                        try:
                            user_choice = int(input("\nChoose your number: "))
                        except ValueError:
                            print("Choose a value as said, number between 1 - 10 (1 and 10 included).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 10:
                            print("Choose a number between 1 - 10")
                            cont -= 1
                            continue

                        if user_choice == number:
                            print("\nCongratulations you got it!")
                            print(f"Total of tries = {cont}")

                            while True:
                                user_answer = input("\nDo you want to keep playing? (Y/N): ").upper()
                                if user_answer in ["Y", "N"]:
                                    break
                                else:
                                    print("Choose Y or N")

                            if user_answer == "Y":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                                continue
                            else:
                                print("\nThank you for playing!")
                                break

                        else:
                            print("Wrong but keep trying!")
                            continue

                case "MEDIUM":
                    print("\nYou are on a number guessing game between 1 - 25 (1 and 25 included).\nGood luck!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

                    while True:
                        try:
                            user_choice = int(input("\nChoose your number: "))
                        except ValueError:
                            print("Choose a value as said, number between 1 - 25 (1 and 25 included).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 25:
                            print("Choose a number between 1 - 25")
                            cont -= 1
                            continue

                        if user_choice > number:
                            print("Lower!")

                        if user_choice < number:
                            print("Higher!")

                        if user_choice == number:
                            print("\nCongratulations you got it!")
                            print(f"Total of tries = {cont}")

                            while True:
                                user_answer = input("\nDo you want to keep playing? (Y/N): ").upper()
                                if user_answer in ["Y", "N"]:
                                    break
                                else:
                                    print("Choose Y or N")

                            if user_answer == "Y":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
                                continue
                            else:
                                print("\nThank you for playing!")
                                break

                        else:
                            print("Wrong but keep trying!")
                            continue
                case "HARD":
                    print("\nYou are on a number guessing game between 1 - 50 (1 and 50 included).\nGood luck!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

                    while True:
                        try:
                            user_choice = int(input("\nChoose your number: "))
                        except ValueError:
                            print("Choose a value as said, number between 1 - 50 (1 and 50 included).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 50:
                            print("Choose a number between 1 - 50")
                            cont -= 1
                            continue

                        if user_choice > number:
                            print("Lower!")

                        if user_choice < number:
                            print("Higher!")

                        if user_choice == number:
                            print("\nCongratulations you got it!")
                            print(f"Total of tries = {cont}")

                            while True:
                                user_answer = input("\nDo you want to keep playing? (Y/N): ").upper()
                                if user_answer in ["Y", "N"]:
                                    break
                                else:
                                    print("Choose Y or N")

                            if user_answer == "Y":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
                                continue
                            else:
                                print("\nThank you for playing!")
                                break

                        else:
                            print("Wrong but keep trying!")
                            continue

        case "PT":
            while True:
                level = input("\nQual dificuldade deseja jogar? FACIL (1-10) - MEDIO (1-25) - DIFICIL (1-50): ").upper()

                if level in ["FACIL", "MEDIO", "DIFICIL"]:
                    break
                else:
                    print("Escolha uma dificuldade")

            match level:
                case "FACIL":
                    print("\nVocê está em um jogo de adivinhação de números entre 1 - 10 (1 e 10 inclusos).\nBoa sorte!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

                    while True:
                        try:
                            user_choice = int(input("\nEscolha seu número: "))
                        except ValueError:
                            print("Escolha um valor como foi dito, número entre 1 - 10 (1 e 10 inclusos).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 10:
                            print("Escolha um número de 1 até 10!")
                            cont -= 1
                            continue

                        if user_choice == number:
                            print("\nParabêns você acertou!")
                            print(f"Total de tentativas = {cont}")

                            while True:
                                user_answer = input("\nVocê deseja continuar jogando? (S/N): ").upper()
                                if user_answer in ["S", "N"]:
                                    break
                                else:
                                    print("Escolha S ou N")

                            if user_answer == "S":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                                continue
                            else:
                                print("\nObrigado por jogar!")
                                break

                        else:
                            print("Errou mas continue tentando!")
                            continue

                case "MEDIO":
                    print("\nVocê está em um jogo de adivinhação de números entre 1 - 25 (1 e 25 inclusos).\nBoa sorte!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

                    while True:
                        try:
                            user_choice = int(input("\nEscolha seu número: "))
                        except ValueError:
                            print("Escolha um valor como foi dito, número entre 1 - 25 (1 e 25 inclusos).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 25:
                            print("Escolha um número de 1 até 25!")
                            cont -= 1
                            continue

                        if user_choice > number:
                            print("Menor!")

                        if user_choice < number:
                            print("Maior!")

                        if user_choice == number:
                            print("\nParabêns você acertou!")
                            print(f"Total de tentativas = {cont}")

                            while True:
                                user_answer = input("\nVocê deseja continuar jogando? (S/N): ").upper()
                                if user_answer in ["S", "N"]:
                                    break
                                else:
                                    print("Escolha S ou N")

                            if user_answer == "S":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
                                continue
                            else:
                                print("\nObrigado por jogar!")
                                break

                        else:
                            print("Errou mas continue tentando!")
                            continue

                case "DIFICIL":
                    print("\nVocê está em um jogo de adivinhação de números entre 1 - 50 (1 e 50 inclusos).\nBoa sorte!")
                    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

                    while True:
                        try:
                            user_choice = int(input("\nEscolha seu número: "))
                        except ValueError:
                            print("Escolha um valor como foi dito, número entre 1 - 50 (1 e 50 inclusos).")
                            continue

                        cont += 1

                        if user_choice < 1 or user_choice > 50:
                            print("Escolha um número de 1 até 50!")
                            cont -= 1
                            continue

                        if user_choice > number:
                            print("Menor!")

                        if user_choice < number:
                            print("Maior!")

                        if user_choice == number:
                            print("\nParabêns você acertou!")
                            print(f"Total de tentativas = {cont}")

                            while True:
                                user_answer = input("\nVocê deseja continuar jogando? (S/N): ").upper()
                                if user_answer in ["S", "N"]:
                                    break
                                else:
                                    print("Escolha S ou N")

                            if user_answer == "S":
                                cont = 0
                                number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23, 24, 25,
                                26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
                                continue
                            else:
                                print("\nObrigado por jogar!")
                                break

                        else:
                            print("Errou mas continue tentando!")
                            continue

        case _:
            print("\nEscolha uma lingugagem como foi dita.")
            print("Choose a language as said.")
            continue

    break
