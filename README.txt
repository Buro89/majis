README

A fun repo to practice some Python data skills and provide some explanation.
I'm uploading fictional scenarios and use cases that are very close to my workplace scenarios.

CASE 1-----------------
Are you a nerd like me that likes to travel with other humans, but also with one's favourite video
game characters (figures, plushies, statues)?
All of them are residents in my house (humans, Asmus figures, plushies and statues) and they're all in 
the complete.xlsx dataset. Some of them were selected to go on a winter trip. Now that summer is 
arriving, a selection for a summer trip has been made, and we need to check if there aren't any residents 
that already joined on the winter trip. Because that wouldn't be fair to those never selected, right!?
However, only Asmus figures are allowed to go on trips twice in a year. For them, being selected
in both the winter and summer isn't against the rules. Some are more equal than others, right??

Files:
- who_is_in_selection.py (code)
- complete.xlsx (dataset with all residents)
- selection_winter.xlsx (dataset with residents selected for winter trip)
- selection_summer.xlsx ("..." summer trip)


CASE 2-----------------
WIP

The residents of my house (from humans to plushies and figures) do x rounds of a game (x is a number YOU 
can decide) where they can win 0 to 10 points in each round.
Alternatively, you -the player- can define your own participants to the game instead of my residents.

All participants are part of a team.

After playing the desired number of rounds, we want to visualise the scores. First of all: in an Excel file,
but also in graphs and even a report!

What we want to plot in graphs, is the following:

- Graph 1 - (WIP) what is the total score for each participant?
- Graph 2 - (WIP) what is the average score for each participant?
- Graph 3 - (WIP) what is the total number of rounds for each participant that they had the top score?
- Graph 4 - (WIP) what is the number of top scores gained within each team, divided by the team size (no. of team members)?
- Graph 5 - (WIP) what is the amount of scores within the teams that are below the average total score? And equal & above?
- Graph 6 - (WIP) what is the average score for each team in Round 1 compared to Round 2? 
- Graph 7 - (WIP) what is the trend in scores across the subsequent rounds for each member of the Majis team?
- Graph 8 - (still to do) what is the trend in scores across the subsequent rounds for each team?

Files:
- dobbelsteen.py (code for generating the scores in each round)
- who_is_in_selection.py (code for data manipulation & plotting the graphs)

These will generate the files:
- dice_scores.xlsx
- dice_scores_processed.xlsx
- Graph1.png until Graph7.png


CASE 3-----------------
WIP
Now we want to generate a nice report of the game results!