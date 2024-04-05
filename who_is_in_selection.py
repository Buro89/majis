# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 2024

@author: Buro89

Case:
Are you a nerd like me that likes to travel with other humans, but also with one's favourite video
game characters (figures, plushies, statues)?
Several entities (humans, Asmus figures, plushies and statues) from the complete.xlsx dataset were 
selected to go on a winter trip. Now that summer is reaching, a selection for a summer trip has been 
made, and we need to check if there aren't any entities that already joined on the winter trip.
Because that wouldn't be fair to those never selected, right!?
However, only Asmus figures are allowed to go on trips twice in a year. For them, being selected
in both the winter and summer isn't against the rules. Some are more equal than others, right??

Dependencies: 
- fsspec 
- openpyxl
(pip install [packagename] in CMD or bash terminal)

Solution: 
Kirby is selected for the summer trip, while also being selected previously for winter.
Kirby is a plushie (type), no Asmus figure, so not allowed to be selected in both seasons.
"""

import pandas as pd
import os

# %%

theChosenPath = os.path.join(os.path.dirname(__file__))

# dataset with the entities selected for winter       = "selection_winter.xlsx"
# "..." summer                                        = "selection_summer.xlsx"

# %%

df_winter     = pd.read_excel(os.path.join(theChosenPath, "selection_winter.xlsx"))
df_summer    = pd.read_excel(os.path.join(theChosenPath, "selection_summer.xlsx"))

# %%

def new_paragraph():
    print("-" * 150)


def print_entities(sample_name):
    if sample_name is df_winter:
        print("-" * 50, "List of those selected for winter:")
    elif sample_name is df_summer:
        print("-" * 50, "List of those selected for summer:")
    else:
        print("Inserted argument is invalid.")
    for entity in sample_name["Name"]:
        print(entity)
    print()

# %%

new_paragraph()
print("These lucky bastards were not only selected for the summer, but also earlier on for last winter!")
double_selection = df_summer["Name"].isin(df_winter["Name"])
entities_in_both = df_summer[double_selection]
print(entities_in_both[["Name", "Type"]])
print()

# %%

new_paragraph()
input("\nPress ENTER to manually double check... ")
print()

print_entities(df_winter)
print_entities(df_summer)

# %%

input("\nPress ENTER to EXIT... ")
