from enum import Enum
class Severity(str, Enum):
    INFO = "Info"
    WARNING = "Warning"
    CRITICAL = "Critical"
class DeliveryType(str, Enum):
    IN_APP = "InApp"
    EMAIL = "Email"
    SMS = "SMS"