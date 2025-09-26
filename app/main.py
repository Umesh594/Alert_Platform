from fastapi import FastAPI
from app.services import alert_service, user_service, analytics_service, reminder_service
app = FastAPI(title="Alerting & Notification Platform")
app.include_router(alert_service.router, prefix="/admin", tags=["Admin"])
app.include_router(user_service.router, prefix="/user", tags=["User"])
app.include_router(analytics_service.router, prefix="/analytics", tags=["Analytics"])
reminder_service.start_scheduler()