from components import vars

def total(value):

    if value == 0:
        vars.character = vars.characters[3]
        print("It's " + vars.character)
    # add some emoji icons, or show the character image

    elif value == 20:
        vars.character = vars.characters[2]
        print("It's " + vars.character)

    elif value == 30:
        vars.character = vars.characters[0]
        print("It's " + vars.character)
        
    else:
        vars.character = vars.characters[1]
        print("It's " + vars.character)
