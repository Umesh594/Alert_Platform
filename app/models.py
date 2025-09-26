from datetime import datetime
from typing import Optional
from app.utils.enums import Severity, DeliveryType
from app.utils.state import AlertState
class Alert:
    def __init__(self, id: int, title: str, message: str, severity: Severity,
                 delivery_type: DeliveryType, start: datetime, expiry: datetime,
                 reminder_frequency: int = 120, visibility: dict = None, reminders_enabled: bool = True):
        self.id = id
        self.title = title
        self.message = message
        self.severity = severity
        self.delivery_type = delivery_type
        self.start = start
        self.expiry = expiry
        self.reminder_frequency = reminder_frequency
        self.visibility = visibility or {"org": True, "teams": [], "users": []}
        self.reminders_enabled = reminders_enabled
class User:
    def __init__(self, id: int, name: str, team_id: int):
        self.id = id
        self.name = name
        self.team_id = team_id
class Team:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
class NotificationDelivery:
    def __init__(self, alert_id: int, user_id: int, timestamp: datetime):
        self.alert_id = alert_id
        self.user_id = user_id
        self.timestamp = timestamp
class UserAlertPreference:
    def __init__(self, user_id: int, alert_id: int, state: AlertState):
        self.user_id = user_id
        self.alert_id = alert_id
        self.state = state
        self.snoozed_until: Optional[datetime] = None