from fastapi import APIRouter, HTTPException
from app.database import users, alerts, user_prefs
from app.schemas import UserOut
from app.utils.state import AlertState
from datetime import datetime
router = APIRouter()
@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(404, "User not found")
    return users[user_id]
@router.get("/{user_id}/alerts")
def get_user_alerts(user_id: int):
    if user_id not in users:
        raise HTTPException(404, "User not found")
    result = []
    for alert in alerts.values():
        pref_key = (user_id, alert.id)
        state = user_prefs.get(pref_key, AlertState.UNREAD)
        result.append({"alert": alert.title, "state": str(state)})
    return result
@router.post("/{user_id}/alerts/{alert_id}/read")
def mark_as_read(user_id: int, alert_id: int):
    user_prefs[(user_id, alert_id)] = AlertState.READ
    return {"msg": f"User {user_id} marked alert {alert_id} as read"}
@router.post("/{user_id}/alerts/{alert_id}/unread")
def mark_as_unread(user_id: int, alert_id: int):
    user_prefs[(user_id, alert_id)] = AlertState.UNREAD
    return {"msg": f"User {user_id} marked alert {alert_id} as unread"}
@router.post("/{user_id}/alerts/{alert_id}/snooze")
def snooze_alert(user_id: int, alert_id: int):
    key = (user_id, alert_id)
    user_prefs[key] = AlertState.SNOOZED
    return {"msg": f"User {user_id} snoozed alert {alert_id} until tomorrow"}