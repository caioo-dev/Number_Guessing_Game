import random


def get_language():
    while True:
        print("\nVocê deseja jogar em qual língua? (EN/PT)")
        print("What language do you want to play? (EN/PT)")
        lang = input("Choose your language: ").upper()

        if lang in ["EN", "PT"]:
            return lang
        else:
            print("Choose a language as said.")


def get_difficulty(lang):
    while True:
        if lang == "EN":
            level = input("\nWhich level do you want to play? EASY (1-10) - MEDIUM (1-25) - HARD (1-50): ").upper()
        else:
            level = input("\nQual dificuldade deseja jogar? FACIL (1-10) - MEDIO (1-25) - DIFICIL (1-50): ").upper()

        if level in ["EASY", "MEDIUM", "HARD", "FACIL", "MEDIO", "DIFICIL"]:
            return level
        else:
            print("Choose a difficulty.")


def generate_number(level):
    if level in ["EASY", "FACIL"]:
        return random.randint(1, 10)
    elif level in ["MEDIUM", "MEDIO"]:
        return random.randint(1, 25)
    elif level in ["HARD", "DIFICIL"]:
        return random.randint(1, 50)


def get_user_input(level):
    while True:
        try:
            user_choice = int(input("\nChoose your number: "))
            if level in ["EASY", "FACIL"]:
                valid_range = range(1, 11)
            elif level in ["MEDIUM", "MEDIO"]:
                valid_range = range(1, 26)
            else:
                valid_range = range(1, 51)

            if user_choice not in valid_range:
                print(f"Choose a value as said, number between 1 - {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10} (1 and {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10} included).")
                continue

        except ValueError:
            print(f"Choose a value as said, number between 1 - {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10} (1 and {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10} included).")
            continue

        return user_choice


def get_game_info(lang, level):
    range_text = f"1 - {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10}"
    range_inclusive = f"1 and {50 if level in ['HARD', 'DIFICIL'] else 25 if level in ['MEDIUM', 'MEDIO'] else 10} included"

    if lang == "EN":
        return f"\nYou are on a number guessing game between {range_text} ({range_inclusive}).\nGood luck!"
    else:
        return f"\nVocê está em um jogo de adivinhação de números entre {range_text} (1 e {range_inclusive} inclusos).\nBoa sorte!"


def get_congratulatory_message(lang):
    if lang == "EN":
        return "\nCongratulations you got it!"
    else:
        return "\nVocê conseguiu parabéns!"


def get_continue_message(lang):
    if lang == "EN":
        return "\nDo you want to keep playing? (Y/N): "
    else:
        return "\nDeseja continuar jogando? (S/N): "


def get_wrong_guess_message(lang, user_choice, number):
    if lang == "EN":
        return ("Lower!" if user_choice > number else "Higher!") + "\nWrong but keep trying!"
    else:
        return ("Menor!" if user_choice > number else "Maior!") + "\nErrou mas continue tentando"


def get_thank_you_message(lang):
    if lang == "EN":
        return "\nThank you for playing!"
    else:
        return "\nObrigado por jogar!"


def play_game(lang, level):
    print(get_game_info(lang, level))

    number = generate_number(level)
    cont = 0

    while True:
        user_choice = get_user_input(level)
        cont += 1

        if user_choice == number:
            print(get_congratulatory_message(lang))
            print(f"Total de tentativas = {cont}")

            while True:
                user_answer = input(get_continue_message(lang)).upper()
                if user_answer in ["Y", "N"]:
                    break
                else:
                    print("Choose Y or N")

            if user_answer == "Y":
                return True
            else:
                print(get_thank_you_message(lang))
                return False

        else:
            print(get_wrong_guess_message(lang, user_choice, number))


def main():
    lang = get_language()

    while True:
        level = get_difficulty(lang)
        if not play_game(lang, level):
            break


if __name__ == "__main__":
    main()
