# ADICIONAR NÍVEIS DE DIFICULDADE, 1-10, 1-20, 1-50
# ADICIONAR "DICAS"
# ADICIONAR ESTATISTICAS DO JOGADOR

import random

cont = 0
# while da linguagem
while True:
    print("\nVocê deseja jogar em qual língua? (EN/PT)")
    print("What language do you want to play? (EN/PT)")
    lang = input("Choose your language: ").upper()
    match lang:

        case "EN":
            print("\nYou are on a number guessing game between 1 - 20 (1 and 20 included).\nGood luck!")
            number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            # while do jogo
            while True:
                try:
                    user_choice = int(input("\nChoose your number: "))
                except ValueError:
                    print("Choose a value as said, number between 1 - 20 (1 and 20 included).")
                    continue

                cont += 1

                if user_choice < 1 or user_choice > 20:
                    print("Choose a number between 1 - 20")
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
                        number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
                        continue
                    else:
                        print("\nThank you for playing!")
                        break

                else:
                    print("Wrong but keep trying!")
                    continue

        case "PT":
            print("\nVocê está em um jogo de adivinhação de números entre 1 - 20 (1 e 20 inclusos).\nBoa sorte!")
            number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            # while do jogo
            while True:
                try:
                    user_choice = int(input("\nEscolha seu número: "))
                except ValueError:
                    print("Escolha um valor como foi dito, número entre 1 - 20 (1 e 20 inclusos).")
                    continue

                cont += 1

                if user_choice < 1 or user_choice > 20:
                    print("Escolha um número de 1 até 20!")
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
                        number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
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

    # break lang
    break
