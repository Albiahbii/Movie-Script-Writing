import os
from datetime import datetime

clear = lambda: os.system('clear')

def script():
    title = input("Enter story title: ").title()
    location = input("Enter Location: ")
    characters = input("Enter comma seperated names of characters: ")
    clear()
    print("'.new' starts a new plot and 'x' exits the script...")
    print(title.center(50))
    characters = characters.split(",")
    characters = [i.strip() for i in characters]
    scene = 1
    Plot = f"\nPlot - {scene} - {location}"
    Characters =  "Characters: " + ",".join(characters) + "\n"
    dialogues = title.center(50) + "\n" + Plot + "\n" + Characters
    print(Plot)
    print(Characters)
    
    run = True
    while run:
        for i in range(len(characters)):
            char = f"{characters[i]}: "
            dialogue = input(char)
            if not dialogue:
                continue
            if dialogue == ".new":
                scene += 1
                print()
                location = input("Enter Location: ")
                characters = input("Enter comma seperated names of characters: ")
                characters = characters.split(",")
                characters = [i.strip() for i in characters]
                Plot = "\n" + f"Plot - {scene} - {location}" + "\nCharacters: " + ",".join(characters) + "\n"
                print(Plot)
                dialogues += "\n" + Plot
                break
            if dialogue == "x":
                run = False
                break
            dialogues += "\n" + char + dialogue
            
    clear()
    print(dialogues)
    now = datetime.now()
    now = datetime.strftime(now, "-%d-%m-%Y")
    with open(f"scripts/{title}{now}.txt", "w") as f:
        f.write(dialogues)

script()

