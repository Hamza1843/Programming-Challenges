import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
            return csv_contents

    
def init_teams(csv_contents):
            teams = {}
            for row in csv_contents:
                home = row[1]
                away = row[2]
                if home not in teams:
                    teams[home]=[0,0]
                if away not in teams:
                    teams[away] = [0,0]
            return teams

def calc_points(teams, csv_contents):
    for row in csv_contents:
        home = row[1]
        away = row[2]
        winner = row[5]
        if winner == "H":
            teams[home][0]+=3
        if winner == "D":
            teams[home][0]+=1
            teams[away][0]+=1
        if winner == "A":
            teams[away][0]+=3
    return teams

def calc_goaldifference(teams, csv_contents):
    for row in csv_contents:
        home = row[1]
        away = row[2]
        home_goals = int(row[3])
        away_goals = int(row[4])
        teams[home][1]+=home_goals
        teams[away][1]+=away_goals
        teams[home][1]-=away_goals
        teams[away][1]-=home_goals
    return teams
if __name__ == "__main__":
    csv_contents = read_csv(csv_file)
    teams=calc_goaldifference(calc_points(init_teams(csv_contents), csv_contents), csv_contents)
    teams=(dict(sorted(teams.items(), key=lambda item: item[1])))
    print(f"""{"#":<5}{"Team":<24}{"PTS":<24}{"GD":<24}""")
    for i in range(19, 0, -1):
        print(f"""{20-(i):<5}{list(teams.items())[i][0]:<24}{list(teams.items())[i][1][0]:<24}{list(teams.items())[i][1][1]:<24}""")
