import json
from models import Team, Driver, Car

def load_teams_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    teams = []
    for team_data in data:
        drivers = [
            Driver(
                name=d["name"],
                number=d["number"],
                nationality=d["nationality"]
            ) for d in team_data["drivers"]
        ]
        car = Car(
            engine=team_data["engine"]
        )
        team = Team(
            name=team_data["team"],
            engine=team_data["engine"],
            drivers=drivers,
            car=car
        )
        teams.append(team)
    return teams

if __name__ == "__main__":
    teams = load_teams_from_json("data/f1_2024_teams.json")
    for team in teams:
        print(team)