from fastapi import APIRouter, HTTPException
from app.database import alerts, alert_id_counter
from app.models import Alert
from app.schemas import AlertCreate, AlertUpdate, AlertOut
from app.utils.enums import Severity, DeliveryType
router = APIRouter()
@router.post("/alerts", response_model=AlertOut)
def create_alert(alert: AlertCreate):
    global alert_id_counter
    new_alert = Alert(
        id=alert_id_counter,
        title=alert.title,
        message=alert.message,
        severity=alert.severity,
        delivery_type=alert.delivery_type,
        start=alert.start,
        expiry=alert.expiry,
        reminder_frequency=alert.reminder_frequency,
        visibility={"org": alert.visibility_org,
                    "teams": alert.visibility_teams,
                    "users": alert.visibility_users},
        reminders_enabled=alert.reminders_enabled,
    )
    alerts[alert_id_counter] = new_alert
    alert_id_counter += 1
    return new_alert
@router.put("/alerts/{alert_id}", response_model=AlertOut)
def update_alert(alert_id: int, update: AlertUpdate):
    if alert_id not in alerts:
        raise HTTPException(404, "Alert not found")
    alert = alerts[alert_id]
    if update.title: alert.title = update.title
    if update.message: alert.message = update.message
    if update.severity: alert.severity = update.severity
    if update.expiry: alert.expiry = update.expiry
    if update.reminders_enabled is not None:
        alert.reminders_enabled = update.reminders_enabled
    return alert
@router.get("/alerts", response_model=list[AlertOut])
def list_alerts():
    return list(alerts.values())