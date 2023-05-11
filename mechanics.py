import logging
from os import system

"""
-----------------------------------------------------
---------- CONSOLE INTERACTIVE NOVEL BETA -----------
------------------- VERSION 1.7 ---------------------
-----------------------------------------------------
developed by ktskm

any further code blocks that look like this would be for documentation.

"""

# general class all classes inherit from.
class General:

    """
    
    general functions to be inherited by all classes
    
    """


    def is_integer(value) -> bool:
        """
        
        checks on if whether the value input is an integer or not

        """


        try:
            value += 1
            return True
        except:
            return False

# character class
class character(General):
    
    """
    
    the character class, which handles the character list
    
    """


    def __init__(self):
        self.charlist = []

    # class specific functions
    def make_character(self, name: str, pos = 'cum') -> None:

        """
        
        Function to create a character within the values given. first value, name, is required. The position value can be ignored as it'll just add the character to the end of the list.
        
        """


        chars = self.charlist
        try: 
            chars.insert(pos, f'{name}')
        except: 
            chars.append(name)
            pos = chars.index(name)

        logging.debug(f'created new chareacter "{name}" at position {pos} ')

    def make_character_txt(self,filename: str) -> bool: 

        """
        
        finds a file specified and reads it for names to automatically put inside of the character list. inside the file should be no spaces, and each name to be seperated with ','.
        
        """

        try:
            with open(filename,"r") as txt:
                charl = txt.read().split(',')
            
            for x in charl:
                self.charlist.append(x)
                logging.debug(f'created new character "{x}" at position {self.charlist.index(x)} ')
            
            return True
        except:
            logging.error(f"INVALID FILE: {filename}. ")
            return False


    def characterName(self,char,mystery=False) -> str:

        """
        
        When called upon checks whether the given value is an index for the character list, or just plain text then return the name resulting from that check. Also changes name into "???" if set mystery to True.
        
        """

        # check if the input character is a index, or string, or if mystery is enabled
        try:
            name = self.charlist[int(char)]
        except:
            if mystery == True:
                name="???"
            else:
                name = char

        return name

class scene(General):

    """
    
    the scene class which is what you'll find yourself most using. it handles the dialogue, to the user input.

    """


    def __init__(self, level: int, user = "user"):
        self.character = character()

        self.choices = []
        self.results = []
        self.user = user
        if level == 1:
            logging.basicConfig(level=logging.DEBUG)
        elif level == 2:
            logging.basicConfig(level=logging.INFO)
        else:
            pass

    def make_choice(self,string: str, pos: int):

        """
        
        creates a option for the player to take. use together with make_result() to make a system of user -> result -> user, etc.
        system works via linked lists. choice 1 and result 1 would be linked because of having the same index number. thats how this CIN system works fundamentally.
        
        """

        self.choices.insert(pos, f'{self.user}: {string}')
        logging.debug(f'at choice position {pos} put line "{string}". ')

    def make_response(self, string: str, pos: int,char: int,mystery = False):
        
        """
        
        creates a option for the player to take. use together with make_choice() to make a system of user -> result -> user, etc.
        system works via linked lists. choice 1 and result 1 would be linked because of having the same index number. thats how this CIN system works fundamentally.
        
        """

        self.results.insert(pos,  f'{self.character.characterName(char,mystery)}: {string}')
        logging.debug(f'at response position {pos} put line "{string}". ')

    def list_response(self):

        """
        
        prints all available choices for the user to take (yes i know its called list_response, and not list_choice.). I advise you to not use it, as it's already being used in commit()

        """

        for x in self.choices:
            print(f'\n  {int(self.choices.index(x)) + 1 } - {x}')

    def clear(self):

        """
        
        clears the choice, and results index. Use this after every commit()
        
        """

        logging.debug(f'cleared choice index, and results index. ')
        self.choices.clear()
        self.results.clear()

    def char_say(self,string: str,char,mystery = False):

        """
        
        get a character to say something.
        
        """

        print(f"{self.character.characterName(char,mystery)}: {string}")
    
    def user_say(self,string):

        """
        
        get the user, or at least the representation of the user, to say something. You can use this for internal monologue.
        
        """

        print(f'{self.user}: {string}')

    def commit(self):

        """
        
        the final thing you should do after setting up your interaction. it'll list down all available options, get in the user's input, and output the result of that choice. Use clear() after this to reuse the same instance.
        
        """


        try:
            self.list_response() # dont be dumb and forget you put list_response() in commit()
            ch = int(input("\n\n"))
            print(self.results[ch - 1])
            return ch
        except:
            logging.error("user tried to put choice that is not in index")
            print("! > that isnt a part of the options. Press enter to continue. < !")
            input()
            system('cls')
            self.commit() # reset commit() after failed commit() 
            