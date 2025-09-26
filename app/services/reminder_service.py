import threading, time
from datetime import datetime
from app.database import alerts, users, user_prefs
from app.services.notif_service import InAppChannel
from app.utils.state import AlertState
def reminder_loop():
    channel = InAppChannel()
    while True:
        now = datetime.now()
        for alert in alerts.values():
            if not alert.reminders_enabled: continue
            if alert.start <= now <= alert.expiry:
                for uid, user in users.items():
                    state = user_prefs.get((uid, alert.id), AlertState.UNREAD)
                    if state == AlertState.UNREAD:
                        channel.send(uid, alert.id, f"Reminder: {alert.title}")
        time.sleep(30)
def start_scheduler():
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()