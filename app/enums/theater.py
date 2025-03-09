import enum

class SpecialEventEnum(str, enum.Enum):
    NONE = "none"
    BIRTHDAY = "birthday"
    LAST_SHOW = "last_show"