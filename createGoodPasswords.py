from sys import argv
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import sample
import pyperclip

class password_generator:
    def __init__(self, length):
        self.length = length
        self.characters = ascii_uppercase + ascii_lowercase + digits + punctuation
    def create_pass(self):
        self.password = ''.join(sample(self.characters, self.length)) 
        pyperclip.copy(self.password)
        return self.password

class draw_title:
    def __init__(self):
        self.logo = """
            ============  =============  =============  =======
            ==            ==         ==  ==         ==  ==     ==
            ==            ==         ==  ==         ==  ==      ==
            ==            ==         ==  ==         ==  ==       ==
            ==   =======  ==         ==  ==         ==  ==       ==
            ==        ==  ==         ==  ==         ==  ==      ==
            ==        ==  ==         ==  ==         ==  ==     ==
            ============  =============  =============  =======
        """ 
    
    def write(self):
        print(self.logo)

    
 

if __name__ == '__main__':
    if (len(argv) < 2 or len(argv) > 2 or (not argv[1].isdecimal())):
        text = '\033[91mdigit your password size'
        print(text.center(60))
        print('\033[92mUsage: python createGoodPasswords.py password_length')
        exit()
    
    password_gen = password_generator(int(argv[1]))
    draw_title().write()

    print(password_gen.create_pass())
    print('\033[92mcopied password to clipboard')

