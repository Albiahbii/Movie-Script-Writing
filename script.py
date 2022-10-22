import os
from datetime import datetime

clear = lambda: os.system('clear')

def script():
    title = input("Enter story title: ").title()
    characters = input("Enter comma seperated names of characters: ")
    clear()
    print("'.new' starts a new plot and 'x' exits the script...")
    print(title.center(50))
    characters = characters.split(",")
    characters = [i.strip() for i in characters]
    scene = 1
    location = input("Enter Location: ")
    Plot = f"Plot - {scene} - {location}"
    dialogues = title.center(50) + "\n" + "Characters: " + ",".join(characters) + "\n\n" + Plot
    print(Plot)
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
                Plot = "\n" + f"Plot - {scene} - {location}"
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

