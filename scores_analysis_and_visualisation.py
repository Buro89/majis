import os
import statistics
from statistics import mean
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

the_chosen_path = os.path.join(os.path.dirname(__file__))

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
    plt.savefig(f"{the_chosen_path}/{filename}.png", dpi=500, transparent=transparency, bbox_inches="tight")
    plt.show()


def print_paragraph(text):
    print("\n\n\n\n", 50 * "*", text, 50 * "*", "\n")

number_of_participants = data.shape[0]
number_of_rounds = data.shape[1] - 3
number_of_team_members = data["Team"].value_counts().sort_index()
largest_team = number_of_team_members.max()

print(f"""Check: 
- you have {number_of_participants} partcipants;
- you have {number_of_rounds} rounds
- you have {largest_team} members in your largest team.")
""")


def determine_max_y_axis(depvar, dataset):
        max_score = dataset[depvar].max()
        max_y_axis = max_score + max_score * 0.2
        return max_y_axis


counter = 0
while counter < 1:
    introtext = input("""
                                Hello. Now we're going to analyse the score data and output some graphs!

                                Press a key to continue! OR type 'stop' to quit! """)

    if introtext.lower() == "stop":
        break
    
    counter += 1

    participant_names = data["Participant"].tolist()
    participant_colors = {
        participant: sns.color_palette("rocket", n_colors=len(participant_names))[i]
        for i, participant in enumerate(participant_names)
    }
    
    
    team_names = data["Team"].tolist()
    team_colors = {
        team: sns.color_palette("rocket", n_colors=len(team_names))[i]
        for i, team in enumerate(team_names)
    }

    round_columns = [f"Round_{round_number}" for round_number in range(1, number_of_rounds + 1)]
    
    data["total_score"] = data[round_columns].sum(axis=1)
    data["average_score"] = data[round_columns].mean(axis=1)

    print_paragraph("Total Score Per Participant:")
    for i in range(1, number_of_participants + 1):
        for index, row in data.iterrows():
            if row["ID"] == i:
                total_score = row["total_score"]
                print(f"{row['Participant']} has a total score of {total_score}")

    print_paragraph("Summary Statistics Total Score Of All Participants:")
    print(get_sumstats("total_score", data))

    print_paragraph("Average Score Per Participant:")
    for i in range(1, number_of_participants + 1):
        for index, row in data.iterrows():
            if row["ID"] == i:
                average_score = row["average_score"]
                print(f"{row['Participant']} has an average score of {average_score}")

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
    
    print_paragraph("Total Times A Participant Had Top Score:")
    for i in range(1, number_of_participants + 1):
        for index, row in data.iterrows():
            if row["ID"] == i:
                total_top_positions = row["total_top_positions"]
                print(f"{row['Participant']} was in the top at {total_top_positions}")

    print_paragraph("Summary Statistics Top Score Occurences Of All Participants:")
    print(get_sumstats("total_top_positions", data))

    team_top_scores_mean = data.groupby("Team")["total_top_positions"].mean().reset_index()
    team_top_scores_mean.columns = ["Team", "Average No. Of Top Scores For Team"]
    teamdata = pd.merge(data, team_top_scores_mean, on="Team")

    print_paragraph("Global Info About The Score Dataframe")
    data.info()
    print(f"\n\n {data.head} \n\n")

    # GRAPH 1


    max_y_axis = determine_max_y_axis("total_score", data)
    sns.set(style="whitegrid", font="Garamond")
    plt.rcParams["font.family"] = "Garamond"
    plt.figure(figsize=(14, 6))
    sns.barplot(data=data, x="Participant", y="total_score", palette=participant_colors, alpha = 0.7, width=1, errorbar = None)
    plt.xlabel("Participant", fontsize=32, labelpad=18)
    plt.ylabel("Total Score", fontsize=32, labelpad=18)
    plt.xticks(fontsize=24, rotation=90)
    plt.yticks(fontsize=24)
    plt.ylim(0, max_y_axis)
    save_and_show_plot("Graph1", False)

    print_paragraph("TABLE - Total Scores Of Participants")
    print_proportion_table_per_group("total_score", "Participant", data)

    # GRAPH 2
    max_y_axis = determine_max_y_axis("average_score", data)
    sns.set(style="whitegrid", font="Garamond")
    plt.rcParams["font.family"] = "Garamond"
    plt.figure(figsize=(14, 6))
    sns.barplot(data=data, x="Participant", y="average_score", palette=participant_colors, alpha = 0.7, width=1, errorbar = None)
    plt.xlabel("Participant", fontsize=32, labelpad=18)
    plt.ylabel("Average Score", fontsize=32, labelpad=18)
    plt.xticks(fontsize=24, rotation=90)
    plt.yticks(fontsize=24)
    plt.ylim(0, max_y_axis)
    save_and_show_plot("Graph2", False)

    print_paragraph("TABLE - Average Scores Of Participants")
    print_proportion_table_per_group("average_score", "Participant", data)

    # GRAPH 3
    max_y_axis = determine_max_y_axis("total_top_positions", data)
    sns.set(style="whitegrid", font="Garamond")
    plt.rcParams["font.family"] = "Garamond"
    plt.figure(figsize=(14, 6))
    sns.barplot(data=data, x="Participant", y="total_top_positions", palette=participant_colors, alpha = 0.7, width=1, errorbar = None)
    plt.xlabel("Participant", fontsize=32, labelpad=18)
    plt.ylabel("Total rounds at top", fontsize=32, labelpad=18)
    plt.xticks(fontsize=24, rotation=90)
    plt.yticks(fontsize=24)
    plt.ylim(0, max_y_axis)
    save_and_show_plot("Graph3", False)

    print_paragraph("TABLE - Total Top Positions for Each Participant")
    print_proportion_table_per_group("total_top_positions", "Participant", data)

    # GRAPH 4

    max_y_axis = determine_max_y_axis("Average No. Of Top Scores For Team", teamdata)
    sns.set(style="whitegrid", font="Garamond")
    plt.rcParams["font.family"] = "Garamond"
    plt.figure(figsize=(14, 9))
    sns.barplot(data=teamdata, x="Team", y="Average No. Of Top Scores For Team", palette=team_colors, alpha = 0.7, width=1, errorbar = None)
    plt.ylabel("Average rounds that team members were at top", fontsize=32, labelpad=18)
    plt.xlabel("Teams", fontsize=32, labelpad=18)
    plt.xticks(fontsize=24, rotation=90)
    plt.yticks(fontsize=24)
    plt.ylim(0, max_y_axis)
    save_and_show_plot("Graph4", False)

    print_paragraph("TABLE - Average rounds that team members were at top")
    print_proportion_table_per_group("Average No. Of Top Scores For Team", "Team", teamdata)

    # GRAPH 5
    average_total_score = data["total_score"].mean()
    data["final_evaluation"] = data["total_score"].apply(lambda x: 1 if x >= average_total_score else 0)
    above_average_score_data = data[data["final_evaluation"] == 1]
    below_average_score_data = data[data["final_evaluation"] == 0]

    max_y_axis = largest_team + largest_team * 0.2
    sns.set(style="whitegrid", font="Garamond")
    plt.rcParams["font.family"] = "Garamond"
    plt.figure(figsize=(14, 9))
    sns.countplot(data=data, x="Team", hue="final_evaluation", dodge=True, palette={0: "#d18e75", 1: "#176482"}, alpha=0.7)
    plt.ylabel("Quantity", fontsize=32, labelpad=18)
    plt.xlabel("Teams", fontsize=32, labelpad=18)
    plt.xticks(fontsize=24, rotation=90)
    plt.yticks(fontsize=24)
    plt.ylim(0, max_y_axis)
    plt.legend(title="Evaluation", loc="upper right", fontsize=22, title_fontsize="24", labels=["Below average", "Above average"])
    save_and_show_plot("Graph5", False)

    print_paragraph("TABLE - Proportion of Scores Above Average per Team")
    print_proportion_table_per_group("final_evaluation", "Team", data)








    #sns.set(style="whitegrid", font="Garamond")
    #plt.rcParams["font.family"] = "Garamond"
    #plt.figure(figsize=(14, 9))

    #sns.barplot(data=data, x="Team", y="total_top_positions", hue="Team", ci=None, palette={"Majis": "#d18e75", "Dragon Team": "#176482", "Baddies": "#89c6b6", "Japanese Plushies": "pink", "Hydrogenpink Plushies": "#F2C6B6", "Phantom Thieves": "orange", "House Lady": "#60272b"}, alpha=0.7)
    #plt.ylabel("Total rounds at top", fontsize=32, labelpad=18)
    #plt.xlabel("Teams", fontsize=32, labelpad=18)
    #plt.xticks(fontsize=24, rotation=90)
    #plt.yticks(fontsize=24)
    #plt.ylim(0, 5)
    #plt.legend(title="Team", loc="upper right", fontsize=22, title_fontsize="24", labels=["Majis", "Dragon Team", "Baddies", "Japanese Plushies", "Hydrogenpink Plushies", "Phantom Thieves", "House Lady"], ncol=3)
    #save_and_show_plot("scores4", False)

    #print_proportion_table_per_group("total_top_positions", "Team", data)


    data.to_excel(os.path.join(the_chosen_path, "dice_scores_processed.xlsx"), index=False)


    input("Press key to end ")

    # Actiepunten:
    # Maak de code mooier met #%# of zoiets en docstring
    # Maak de grafieken nog mooier! Legenda wel of niet. Kleuren goed?
    # De twee andere grafieken ook nog doen (Graph 6 en 7)
    # Kijken waar meer functies kunnen worden gedefinieerd.
    # Tabellen bepalen: wat wil je in tabellen in de report
    # Report maken met tabellen, grafieken en tekst. Allemaal geautomatiseerd!
    # Kijk of je code HELEMAAL object oriented kan! En efficienter.
