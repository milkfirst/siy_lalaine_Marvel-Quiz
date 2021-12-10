from components.vars import database

def tally(answer, value):
    if answer == "y":
        ans = True
    else:
        ans = False

    remove_data=[]
    for a in database:
        if a[value] != ans:
            remove_data.append(a)

    for b in remove_data:
        database.remove(b)
    
    if len(database) == 1:
        print("I bet your character is "+database[0]["name"]+"! "+"\U0001f600")
        quit()