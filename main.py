import random as rm

#строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

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

    def value_password(self, cntPw):
        pass

    def len_password(self, lenPw):
        pass

    def digit(self, digOn):
        pass

    def lowercase(self, abcOn):
        pass

    def uppercase(self, ABCon):
        pass

    def punctations(self, chOn):
        pass

    def exc(self, excOn):
        pass

class UserInput:
    def __init__(self):
        self.excOn = None
        self.chOn = None
        self.abcOn = None
        self.ABCon = None
        self.digOn = None
        self.lenPw = None
        self.cntPw = None

    def valid_input(self):

        print('-----Генератор Паролей-----')

        self.cntPw = input('Укажите количество паролей для генерации:')
        self.lenPw = input('Укажите длину одного пароля:')
        self.digOn = input('Включать ли цифры 0123456789? (y/n)')
        self.ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
        self.abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
        self.chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
        self.excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
