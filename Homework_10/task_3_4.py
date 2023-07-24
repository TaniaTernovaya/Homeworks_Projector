import csv
import random

PLAYER_NAME = "Player_name"
SCORE = "Score"
HIGH_SCORE = "High_Score"
names = ["Alex", "John", "Robert", "Peter", "Micheal"]
data = []
for i in range(100):
    for name in names:
        score = random.randint(1, 1000)
        data.append({PLAYER_NAME: name, SCORE: score})

header1 = [PLAYER_NAME, SCORE]
with open("game.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=header1)
    writer.writeheader()
    writer.writerows(data)


with open("game.csv", "r") as file:
    reader = csv.DictReader(file)
    high_score = {}
    for row in reader:
        if row[PLAYER_NAME] in high_score.keys():
            if row[SCORE] > high_score[row[PLAYER_NAME]]:
                high_score[row[PLAYER_NAME]] = row[SCORE]
        else:
            high_score[row[PLAYER_NAME]] = row[SCORE]

result = [
    {PLAYER_NAME: name, HIGH_SCORE: high_score}
    for name, high_score in high_score.items()
]

header2 = [PLAYER_NAME, HIGH_SCORE]
with open("high_scores.csv", "w") as high_file:
    writer = csv.DictWriter(high_file, fieldnames=header2)
    writer.writeheader()
    writer.writerows(result)
