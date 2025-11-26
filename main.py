import random as rm

# строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_chars = 'il1Lo0O'


class PasswordGenerator:
    def __init__(self):
        self.cntPw = 0
        self.lenPw = 0
        self.digOn = False
        self.abcOn = False
        self.ABCon = False
        self.chOn = False
        self.excOn = False
        self.chars = ''

        self.available_digits = digits
        self.available_lowercase = lowercase_letters
        self.available_uppercase = uppercase_letters
        self.available_punctuation = punctuation

    def set_password_count(self, cntPw):
        try:
            self.cntPw = int(cntPw)
            return True
        except ValueError:
            print("Ошибка: введите число для количества паролей")
            return False

    def set_password_length(self, lenPw):
        try:
            self.lenPw = int(lenPw)
            return True
        except ValueError:
            print("Ошибка: введите число для длины пароля")
            return False

    def digit(self, digOn):
        self.digOn = digOn.lower() == "y"

    def lowercase(self, abcOn):
        self.abcOn = abcOn.lower() == "y"

    def uppercase(self, ABCon):
        self.ABCon = ABCon.lower() == "y"

    def punctations(self, chOn):
        self.chOn = chOn.lower() == "y"

    def exc(self, excOn):
        self.excOn = excOn.lower() == "y"

    def prepare_character_sets(self):
        if self.excOn:
            for char in ambiguous_chars:
                self.available_digits = self.available_digits.replace(char, '')
                self.available_lowercase = self.available_lowercase.replace(char, '')
                self.available_uppercase = self.available_uppercase.replace(char, '')
                self.available_punctuation = self.available_punctuation.replace(char, '')

    def build_password(self):
        self.chars = ""
        selected_categories = []

        if self.digOn:
            self.chars += self.available_digits
            selected_categories.append(self.available_digits)

        if self.abcOn:
            self.chars += self.available_lowercase
            selected_categories.append(self.available_lowercase)

        if self.ABCon:
            self.chars += self.available_uppercase
            selected_categories.append(self.available_uppercase)

        if self.chOn:
            self.chars += self.available_punctuation
            selected_categories.append(self.available_punctuation)

        # Проверяем что есть хотя бы один символ
        if not self.chars:
            print("Ошибка: не выбран ни один тип символов!")
            return False

        # Проверяем что длина пароля достаточна для всех категорий
        if self.lenPw < len(selected_categories):
            print(
                f"Ошибка: длина пароля ({self.lenPw}) слишком мала для выбранных категорий ({len(selected_categories)})")
            return False

        return True

    def generate_secure_password(self):
        password_chars = []

        if self.digOn and self.available_digits:
            password_chars.append(rm.choice(self.available_digits))

        if self.abcOn and self.available_lowercase:
            password_chars.append(rm.choice(self.available_lowercase))

        if self.ABCon and self.available_uppercase:
            password_chars.append(rm.choice(self.available_uppercase))

        if self.chOn and self.available_punctuation:
            password_chars.append(rm.choice(self.available_punctuation))

        remaining_length = self.lenPw - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(rm.choice(self.chars))

        rm.shuffle(password_chars)

        return ''.join(password_chars)

    def generate_passwords(self):
        self.prepare_character_sets()

        if not self.build_password():
            return []

        passwords = []
        for _ in range(self.cntPw):
            passwords.append(self.generate_secure_password())
        return passwords


class UserInput:
    def __init__(self):
        self.cntPw = ''
        self.lenPw = ''
        self.digOn = ''
        self.ABCon = ''
        self.abcOn = ''
        self.chOn = ''
        self.excOn = ''

    def get_input(self):
        print('-----Генератор Паролей-----')

        self.cntPw = input('Укажите количество паролей для генерации: ')
        self.lenPw = input('Укажите длину одного пароля: ')
        self.digOn = input('Включать ли цифры 0123456789? (y/n): ')
        self.ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
        self.abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
        self.chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
        self.excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')

    def validate_input(self):
        if not all([self.cntPw, self.lenPw, self.digOn, self.ABCon, self.abcOn, self.chOn, self.excOn]):
            print("Ошибка: нужно ответить на все вопросы!")
            return False

        for answer in [self.digOn, self.ABCon, self.abcOn, self.chOn, self.excOn]:
            if answer.lower() not in ['y', 'n']:
                print("Ошибка: на вопросы нужно отвечать 'y' или 'n'!")
                return False

        try:
            cnt = int(self.cntPw)
            length = int(self.lenPw)
            if cnt <= 0 or length <= 0:
                print("Ошибка: количество и длина должны быть положительными числами!")
                return False
        except ValueError:
            print("Ошибка: количество и длина должны быть числами!")
            return False

        return True


def main():
    user_input = UserInput()
    user_input.get_input()

    if not user_input.validate_input():
        return

    generator = PasswordGenerator()

    if not generator.set_password_count(user_input.cntPw):
        return

    if not generator.set_password_length(user_input.lenPw):
        return

    generator.digit(user_input.digOn)
    generator.uppercase(user_input.ABCon)
    generator.lowercase(user_input.abcOn)
    generator.punctations(user_input.chOn)
    generator.exc(user_input.excOn)

    passwords = generator.generate_passwords()

    if passwords:
        print("\n-------Пароли-------")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")


if __name__ == "__main__":
    main()