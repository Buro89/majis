import os
import statistics
from statistics import mean
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

the_chosen_path = "C://Users//Karlijn//Documents//Python_Developer//matplotlib_fullcourse//majis//"

data     = pd.read_excel(os.path.join(the_chosen_path, "dice_scores.xlsx"))


def print_proportion_table(var_name, dataset):
    print("")
    print(f"Proportions for {var_name}")
    print((dataset[var_name].value_counts().sort_index()) / len(dataset[var_name]))
    print("")


def print_proportion_table_per_group(var_name, group_name, dataset):
    for group_name, group_df in dataset.groupby(group_name):
        print(f"Proportions for {group_name}:")
        print((group_df[var_name].value_counts().sort_index()) / len(group_df[var_name]))
        print()


def get_sumstats(var_name, dataset):
    return f""" Mean {var_name}\t\t{dataset[var_name].mean()}
           Std.dev {var_name}\t\t{dataset[var_name].std()}
           Median {var_name}\t\t{dataset[var_name].median()}
           Min {var_name}\t\t{dataset[var_name].min()}
           Max {var_name}\t\t{dataset[var_name].max()}"""


def save_and_show_plot(filename, transparency):
    plt.savefig(f"{the_chosen_path}{filename}.png", dpi=500, transparent=transparency, bbox_inches="tight")
    plt.show()


number_of_rounds = int(input("""
                             Hello. Now we're going to analyse the score data and output some graphs!

                             But first of all, we need some info from you: How many rounds did you play?
                             Don't remember because you were just passionately smashing 'yes' all the time? Then, 
                             open "dice_scores.xlsx and see how many Round_x columns there are (where x is a number).
                             
                             Please insert the number of rounds: """))
round_columns = [f"Round_{round_number}" for round_number in range(1, number_of_rounds + 1)]
data["total_score"] = data[round_columns].sum(axis=1)
print("Total score per participant:")
for i in range(1, 21):
    for index, row in data.iterrows():
        if row["ID"] == i:
            total_score = row["total_score"]
            print(f"{row['Participant']} has a total score of {total_score}")

print(get_sumstats("total_score", data))




average_total_score = data["total_score"].mean()
data["final_evaluation"] = data["total_score"].apply(lambda x: 1 if x >= average_total_score else 0)

for i in range(1, 21):
    for index, row in data.iterrows():
        if row["ID"] == i:
            total_score = row["total_score"]
            print(f"{row['Participant']} has a total score of {total_score}")


for i in range(1, number_of_rounds + 1):
    globals()[f"highest_round{i}"] = data[f"Round_{i}"].max()
    data[f"top_participant{i}"] = (data[f"Round_{i}"] == globals()[f"highest_round{i}"])

rank_mapping = {
    False: 0,
    True: 1}
for i in range(1, number_of_rounds + 1):
    data[f"top_participant{i}_dummy"] = data[f"top_participant{i}"].map(rank_mapping)
    data[f"top_participant{i}_dummy"] = data[f"top_participant{i}_dummy"].astype(int)

top_position_columns = [f"top_participant{round_number}_dummy" for round_number in range(1, number_of_rounds + 1)]
data["total_top_positions"] = data[top_position_columns].sum(axis=1)
print("Total times a participant was at top position in all rounds:")
for i in range(1, 21):
    for index, row in data.iterrows():
        if row["ID"] == i:
            total_top_positions = row["total_top_positions"]
            print(f"{row['Participant']} was in the top at {total_top_positions}")

print(get_sumstats("total_top_positions", data))


# General overview of the dataframe
print("\n\n" + (10*"-") + "Global info about the dataframe" + (10*"-") + "\n\n")
data.info()
print(f"\n\n {data.head} \n\n")


sns.set(style="whitegrid", font="Garamond")
plt.rcParams["font.family"] = "Garamond"
plt.figure(figsize=(14, 9))

above_average_score_data = data[data["final_evaluation"] == 1]
below_average_score_data = data[data["final_evaluation"] == 0]

sns.countplot(data=data, x="Team", hue="final_evaluation", dodge=True, palette={0: "#d18e75", 1: "#176482"}, alpha=0.7)
plt.ylabel("Quantity", fontsize=32, labelpad=18)
plt.xlabel("Teams", fontsize=32, labelpad=18)
plt.xticks(fontsize=24, rotation=90)
plt.yticks(fontsize=24)
plt.ylim(0, 5)
plt.legend(title="Evaluation", loc="upper right", fontsize=22, title_fontsize="24", labels=["Below average", "Above average"])
#save_and_show_plot("scores", False)

print_proportion_table_per_group("final_evaluation", "Team", data)


sns.set(style="whitegrid", font="Garamond")
plt.rcParams["font.family"] = "Garamond"
plt.figure(figsize=(14, 6))

sns.barplot(data=data, x="Participant", y="total_score", palette={"Cyber": "#d18e75", "Futaba": "#176482", "Okita": "pink", "Nagakura": "#F2C6B6", "Jokah": "#89c6b6", "Yamai": "#60272b", "Karola": "#af793d", "Goromi": "orange", "Kirby": "#5ea46b", "Nozomi": "red", "Bunchan": "#60cea4", "Inizio": "brown", "Star": "black", "Nishitani" :"salmon", "Saejima": "darkgreen", "Altan": "lightblue", "Ryoma": "lightgreen", "Sasaki": "#321B12", "Majima": "#34504e", "Kiryu": "#0f3c48"}, alpha = 0.7, width=1)
plt.xlabel("Participant", fontsize=32, labelpad=18)
plt.ylabel("Total Score", fontsize=32, labelpad=18)
plt.xticks(fontsize=24, rotation=90)
plt.yticks(fontsize=24)
plt.ylim(0, 110)
#save_and_show_plot("scores2", False)


print_proportion_table_per_group("total_score", "Participant", data)



sns.set(style="whitegrid", font="Garamond")
plt.rcParams["font.family"] = "Garamond"
plt.figure(figsize=(14, 6))

sns.barplot(data=data, x="Participant", y="total_top_positions", palette={"Cyber": "#d18e75", "Futaba": "#176482", "Okita": "pink", "Nagakura": "#F2C6B6", "Jokah": "#89c6b6", "Yamai": "#60272b", "Karola": "#af793d", "Goromi": "orange", "Kirby": "#5ea46b", "Nozomi": "red", "Bunchan": "#60cea4", "Inizio": "brown", "Star": "black", "Nishitani" :"salmon", "Saejima": "darkgreen", "Altan": "lightblue", "Ryoma": "lightgreen", "Sasaki": "#321B12", "Majima": "#34504e", "Kiryu": "#0f3c48"}, alpha = 0.7, width=1)
plt.xlabel("Participant", fontsize=32, labelpad=18)
plt.ylabel("Total rounds at top", fontsize=32, labelpad=18)
plt.xticks(fontsize=24, rotation=90)
plt.yticks(fontsize=24)
plt.ylim(0, 6)
#save_and_show_plot("scores3", False)


print_proportion_table_per_group("total_top_positions", "Participant", data)


sns.set(style="whitegrid", font="Garamond")
plt.rcParams["font.family"] = "Garamond"
plt.figure(figsize=(14, 9))

sns.barplot(data=data, x="Team", y="total_top_positions", hue="Team", ci=None, palette={"Majis": "#d18e75", "Dragon Team": "#176482", "Baddies": "#89c6b6", "Japanese Plushies": "pink", "Hydrogenpink Plushies": "#F2C6B6", "Phantom Thieves": "orange", "House Lady": "#60272b"}, alpha=0.7)
plt.ylabel("Total rounds at top", fontsize=32, labelpad=18)
plt.xlabel("Teams", fontsize=32, labelpad=18)
plt.xticks(fontsize=24, rotation=90)
plt.yticks(fontsize=24)
plt.ylim(0, 5)
plt.legend(title="Team", loc="upper right", fontsize=22, title_fontsize="24", labels=["Majis", "Dragon Team", "Baddies", "Japanese Plushies", "Hydrogenpink Plushies", "Phantom Thieves", "House Lady"], ncol=3)
save_and_show_plot("scores4", False)

print_proportion_table_per_group("total_top_positions", "Team", data)


data.to_excel(os.path.join(the_chosen_path, "dice_scores_processed.xlsx"), index=False)

input("Press key to end ")

# Actiepunten:
# Maak de grafieken nog mooier! Legenda op perfecte plek, andere twee grafieken ook een legenda
# 'Trendgrafiek van de Majis van hoe goed zij scoren door de loop van alle rondes heen
# Alle grafieken en tevens tabellen naar een Word document pipen, met nog wat tekst erbij! Allemaal geautomatiseerd!
# Deze code wat netter maken
# dobbelsteen.py naar scores_analyses_and_visualisation.py laten overgaan