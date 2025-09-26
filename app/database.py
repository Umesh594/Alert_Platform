from typing import Dict, List
from app.models import Alert, User, Team, NotificationDelivery, UserAlertPreference
alerts: Dict[int, Alert] = {}
users: Dict[int, User] = {}
teams: Dict[int, Team] = {}
deliveries: List[NotificationDelivery] = []
user_prefs: Dict[tuple, UserAlertPreference] = {} 
alert_id_counter = 1
user_id_counter = 1
team_id_counter = 1
def seed_data():
    global user_id_counter, team_id_counter
    team_eng = Team(id=team_id_counter, name="Engineering")
    teams[team_id_counter] = team_eng
    team_id_counter += 1
    team_mkt = Team(id=team_id_counter, name="Marketing")
    teams[team_id_counter] = team_mkt
    team_id_counter += 1
    users[user_id_counter] = User(id=user_id_counter, name="Alice", team_id=1)
    user_id_counter += 1
    users[user_id_counter] = User(id=user_id_counter, name="Bob", team_id=1)
    user_id_counter += 1
    users[user_id_counter] = User(id=user_id_counter, name="Charlie", team_id=2)
    user_id_counter += 1
seed_data()