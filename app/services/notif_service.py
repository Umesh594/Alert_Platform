from datetime import datetime
from app.models import NotificationDelivery
from app.database import deliveries
class NotificationChannel:
    def send(self, user_id: int, alert_id: int, message: str):
        raise NotImplementedError
class InAppChannel(NotificationChannel):
    def send(self, user_id: int, alert_id: int, message: str):
        deliveries.append(NotificationDelivery(alert_id, user_id, datetime.now()))
        print(f"[InApp] Sent to User {user_id}: {message}")