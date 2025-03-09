import enum

class TicketTypeEnum(str, enum.Enum):
    OFC = "OFC"
    GENERAL = "GENERAL"

class StatusEnum(str, enum.Enum):
    WIN = "win"
    LOSE = "lose"
    PENDING = "pending"