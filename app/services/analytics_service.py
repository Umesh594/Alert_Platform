from fastapi import APIRouter
from app.database import alerts, deliveries, user_prefs
from app.utils.state import AlertState
from collections import Counter
router = APIRouter()
@router.get("/")
def analytics():
    total_alerts = len(alerts)
    delivered = len(deliveries)
    states = Counter(user_prefs.values())
    severity_count = Counter([a.severity for a in alerts.values()])
    return {
        "total_alerts": total_alerts,
        "delivered": delivered,
        "read": states.get(AlertState.READ, 0),
        "unread": states.get(AlertState.UNREAD, 0),
        "snoozed": states.get(AlertState.SNOOZED, 0),
        "severity_breakdown": severity_count,
    }