from enum import Enum
class AlertState(str, Enum):
    UNREAD = "Unread"
    READ = "Read"
    SNOOZED = "Snoozed"