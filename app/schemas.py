from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.utils.enums import Severity, DeliveryType
class AlertCreate(BaseModel):
    title: str
    message: str
    severity: Severity
    delivery_type: DeliveryType = DeliveryType.IN_APP
    start: datetime
    expiry: datetime
    reminder_frequency: int = 120
    visibility_org: bool = True
    visibility_teams: Optional[List[int]] = []
    visibility_users: Optional[List[int]] = []
    reminders_enabled: bool = True
class AlertUpdate(BaseModel):
    title: Optional[str]
    message: Optional[str]
    severity: Optional[Severity]
    expiry: Optional[datetime]
    reminders_enabled: Optional[bool]
class AlertOut(BaseModel):
    id: int
    title: str
    message: str
    severity: Severity
    delivery_type: DeliveryType
    start: datetime
    expiry: datetime
    reminders_enabled: bool
class UserOut(BaseModel):
    id: int
    name: str
    team_id: int