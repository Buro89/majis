import os
from statistics import mean
import random
import pandas as pd

working_dir = os.path.join(os.path.dirname(__file__))
#print(f"----------------------- CHECK: You are currently working in {working_dir}")

relative_path = os.path.join("folder",)

class Residents:
    def __init__(self):
        self.scores = []

    def get_average_score(self):
        return mean(self.scores)

def throw_dice_for_all(participants):
    for participant in participants:
        participant.dice = random.randint(0, 10)
        participant.scores.append(participant.dice)
        print(f"{participant.name} has thrown a {participant.dice}")


resident1 = Residents()
resident1.id = 1
resident2 = Residents()
resident2.id = 2
resident3 = Residents()
resident3.id = 3
resident4 = Residents()
resident4.id = 4
resident5 = Residents()
resident5.id = 5
resident6 = Residents()
resident6.id = 6
resident7 = Residents()
resident7.id = 7
resident8 = Residents()
resident8.id = 8
resident9 = Residents()
resident9.id = 9
resident10 = Residents()
resident10.id = 10
resident11 = Residents()
resident11.id = 11
resident12 = Residents()
resident12.id = 12
resident13 = Residents()
resident13.id = 13
resident14 = Residents()
resident14.id = 14
resident15 = Residents()
resident15.id = 15
resident16 = Residents()
resident16.id = 16
resident17 = Residents()
resident17.id = 17
resident18 = Residents()
resident18.id = 18
resident19 = Residents()
resident19.id = 19
resident20 = Residents()
resident20.id = 20

preference = ""
while preference.upper() != "A" and preference.upper() != "B":
    preference = input("""Let the residents of my house participate, or choose other participants?
                    A. Residents
                    B. Define my own """)
if preference.upper() not in ["A", "B"]:
    print("\nYou didn't answer A or B. Try again.\n")
elif preference.upper() == "B":
    number_of_participants_entered = 0
    command = ""
    while command.upper() != "B":
        for i in range(1, 21):
            name = input(f"Participant{i}'s name: ")
            if name:
                number_of_participants_entered += 1
                globals()[f"resident{i}"].name = name
                globals()[f"resident{i}"].team = input(f"Choose a Team for Participant{i}: ")
                if number_of_participants_entered >= 2:
                    command = input("""Do you want to enter more new participants?
                                    A. continue entering
                                    B. no, let's get to the actual game """)
                    if command.upper() == "B":
                        break
elif preference.upper() == "A":
    number_of_participants_entered = 20
    resident1.name = "Altan"
    resident1.team = "Majis"
    resident2.name = "Goromi"
    resident2.team = "Majis"
    resident3.name = "Kiryu"
    resident3.team = "Dragon Team"
    resident4.name = "Nozomi"
    resident4.team = "Majis"
    resident5.name = "Inizio"
    resident5.team = "Majis"
    resident6.name = "Cyber"
    resident6.team = "Majis"
    resident7.name = "Yamai"
    resident7.team = "Baddies"
    resident8.name = "Sasaki"
    resident8.team = "Baddies"
    resident9.name = "Okita"
    resident9.team = "Japanese Plushies"
    resident10.name = "Ryoma"
    resident10.team = "Japanese Plushies"
    resident11.name = "Saejima"
    resident11.team = "Hydrogenpink Plushies"
    resident12.name = "Nagakura"
    resident12.team = "Japanese Plushies"
    resident13.name = "Futaba"
    resident13.team = "Phantom Thieves"
    resident14.name = "Jokah"
    resident14.team = "Phantom Thieves"
    resident15.name = "Star"
    resident15.team = "Japanese Plushies"
    resident16.name = "Majima"
    resident16.team = "Hydrogenpink Plushies"
    resident17.name = "Karola"
    resident17.team = "House Lady"
    resident18.name = "Nishitani"
    resident18.team = "Baddies"
    resident19.name = "Bunchan"
    resident19.team = "Japanese Plushies"
    resident20.name = "Kirby"
    resident20.team = "Japanese Plushies"
    pass
else:
    print("\nError: Something went wrong. Try again.\n")

participants = []
for i in range(1, number_of_participants_entered + 1):
    participants.append(globals()[f"resident{i}"])

run_another_round = True
while run_another_round:
    throw_dice_for_all(participants)

    max_dice = float('-inf')
    max_resident = []

    for resident in participants:
        if resident.dice > max_dice:
            max_dice = resident.dice
            max_resident = [resident]
        elif resident.dice == max_dice:
            max_resident.append(resident)

    if len(max_resident) == 1:
        print(f"\n\nThe participant with the highest score is {max_resident[0].name} with a score of {max_resident[0].dice}.")
    else:
        print(f"\n\nThe participants with the highest score are:")
        for participant in max_resident:
            print(f"{participant.name} with a score of {participant.dice}.")

    choice = input("Do you want to run another round? (Yes/No): ")
    if choice.lower() != "yes":
        run_another_round = False

print("\n\nOkay cool. The game was fun. Now we'll construct the dataframe. See file 'dice_scores.xlsx'\n\n")

data = {"Participant": [participant.name for participant in participants],
        "ID":  [participant.id for participant in participants],
        "Team": [participant.team for participant in participants]}
number_of_rounds = len(participants[0].scores)

for i in range(1, number_of_rounds + 1):
    round_scores = [participant.scores[i - 1] for participant in participants]
    data[f"Round_{i}"] = round_scores

df = pd.DataFrame(data)

df.to_excel(os.path.join(working_dir, "dice_scores.xlsx"), index=False)

print("\n\nDataframe created... Now generating the scores' results...\n\n")
import scores_analysis_and_visualisation
scores_analysis_and_visualisation


