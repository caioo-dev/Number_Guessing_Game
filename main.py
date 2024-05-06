# ADICIONAR LINGUAGEM INGLÊS PARA A APLICAÇÃO
# ADICIONAR NÍVEIS DE DIFICULDADE, 1-10, 1-20, 1-50
# ADICIONAR "DICAS"
# ADICIONAR ESTATISTICAS DO JOGADOR

import random

print("Você está em um jogo de adivinhação de números entre 1 - 20 (1 e 20 inclusos).\nBoa sorte!")

cont = 0
while True:
    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
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

        user_answer = input("\nDeseja continuar? (S/N): ").upper()

        if user_answer == "S":
            cont = 0
            continue
        else:
            print("\nObrigado por jogar!")
            break

    else:
        print("Errou mas continue tentando!")
        continue
