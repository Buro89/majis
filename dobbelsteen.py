import os
from statistics import mean
import random
import pandas as pd

working_dir = "C://Users//Karlijn//Documents//Python_Developer//matplotlib_fullcourse//majis"

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
resident1.name = "Altan"
resident1.id = 1
resident1.team = "Majis"
resident2 = Residents()
resident2.name = "Goromi"
resident2.id = 2
resident2.team = "Majis"
resident3 = Residents()
resident3.name = "Kiryu"
resident3.id = 3
resident3.team = "Dragon Team"
resident4 = Residents()
resident4.name = "Nozomi"
resident4.id = 4
resident4.team = "Majis"
resident5 = Residents()
resident5.name = "Inizio"
resident5.id = 5
resident5.team = "Majis"
resident6 = Residents()
resident6.name = "Cyber"
resident6.id = 6
resident6.team = "Majis"
resident7 = Residents()
resident7.name = "Yamai"
resident7.id = 7
resident7.team = "Baddies"
resident8 = Residents()
resident8.name = "Sasaki"
resident8.id = 8
resident8.team = "Baddies"
resident9 = Residents()
resident9.name = "Okita"
resident9.id = 9
resident9.team = "Japanese Plushies"
resident10 = Residents()
resident10.name = "Ryoma"
resident10.id = 10
resident10.team = "Japanese Plushies"
resident11 = Residents()
resident11.name = "Saejima"
resident11.id = 11
resident11.team = "Hydrogenpink Plushies"
resident12 = Residents()
resident12.name = "Nagakura"
resident12.id = 12
resident12.team = "Japanese Plushies"
resident13 = Residents()
resident13.name = "Futaba"
resident13.id = 13
resident13.team = "Phantom Thieves"
resident14 = Residents()
resident14.name = "Jokah"
resident14.id = 14
resident14.team = "Phantom Thieves"
resident15 = Residents()
resident15.name = "Star"
resident15.id = 15
resident15.team = "Japanese Plushies"
resident16 = Residents()
resident16.name = "Majima"
resident16.id = 16
resident16.team = "Hydrogenpink Plushies"
resident17 = Residents()
resident17.name = "Karola"
resident17.id = 17
resident17.team = "House Lady"
resident18 = Residents()
resident18.name = "Nishitani"
resident18.id = 18
resident18.team = "Baddies"
resident19 = Residents()
resident19.name = "Bunchan"
resident19.id = 19
resident19.team = "Japanese Plushies"
resident20 = Residents()
resident20.name = "Kirby"
resident20.id = 20
resident20.team = "Japanese Plushies"

participants = [resident1, resident2, resident3, resident4, resident5, resident6, resident7, resident8, resident9, resident10, resident11, resident12, resident13, resident14, resident15, resident16, resident17, resident18, resident19, resident20]

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
        print(f"\n\nThe maji with the highest score is {max_resident[0].name} with a score of {max_resident[0].dice}.")
    else:
        print(f"\n\nThe majis with the highest score are:")
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

# More about creating dataframes from list https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/
Residents()
