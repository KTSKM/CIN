import mechanics
from sys import argv

# debug level check 
if len(argv) > 1:
    if argv[1] == "2":
        level = 2
    elif argv[1] == "1":
        level = 1
    else: pass
else:
    level = 0

# the actual rpg


intro = mechanics.scene(level)
intro.character.make_character_txt('charlist.txt')

intro.char_say(": Well hello... User.",1,True)
intro.make_choice("well hello... person. ",1)
intro.make_response("you can just call me GenMa. :)",1,0)

intro.commit()
intro.clear()

intro.make_choice(f"so... {intro.character.characterName(0)}, what is this place? ",1)
intro.make_response(f'Uhm.. Its your computer obviously. There would probably be a paragraph said by you in first person describing the place, however the current writer isnt exactly skilled enough for that.',1,0)

intro.make_choice(f'Then hello GenMa..',2)
intro.make_response("That's it? You're a horrible conversationalist you know.",2,0)

ch = intro.commit()
# commit returns the choice the user put in, so we can use it like this to make 'routes'
intro.clear()
if ch == 1:
    intro.make_choice("meta much?",1)
    intro.make_response("What'd you expect?",1,0)

    intro.make_choice("wow so funny....",2)
    intro.make_response("Don't be sarcastic, i'm sure the writer is an amazing person!",2,0)

    intro.make_choice("Thats a lot of words, that i'm not reading!",3)
    intro.make_response("Then why the hell would you run this  CONSOLE INTERACTIVE NOVEL  if you dont wanna read text.",3,0)
else:
    intro.make_choice("You're not any good either..",1)
    intro.make_response("At least im trying.",1,0)

    intro.make_choice("And you're rude. ",2)
    intro.make_response("Well sorry i guess.",2,0)

intro.commit()
# Tip! :  always make sure to commit() after every change so the user would actually see and do stuff withthe stuff you wrote.

smthn = mechanics.scene(level) # this adds characters via code, without the use of a charlist.txt
smthn.character.make_character('GenMa',0)
smthn.character.make_character('Stik')

smthn.char_say(": oh theres someone else here",0)


smthn.make_choice("huh who?",1)
smthn.make_response("Me of course!", 1, 1,True) # new character, Stik

smthn.commit()

smthn.char_say(f"I'm {smthn.character.characterName(1)}! Tottally not a ripoff!", 1, False)
smthn.clear()

smthn.user_say("Okay im too lazy to write anything more. Thats it good job you reached the end.")

