
def check_nickname(nickname: str):
    '''
    никнейм должен начинаться с символа @
    никнейм должен содержать от 5 до 15 (включительно) символов (включая первый символ @)
    никнейм должен содержать только строчные буквы и цифры (помимо первого символа @)
    '''

    if 5 <= len(nickname) <= 15 and nickname[0] == "@" and nickname[1:].isalnum() and (
            nickname.islower() or nickname[1:].isdigit()):
        return "Correct"
    else:
        return "Incorrect"


print(check_nickname("@paula"))
