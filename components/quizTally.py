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
    

    
