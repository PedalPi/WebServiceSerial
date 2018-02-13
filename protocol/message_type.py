from enum import Enum


class Verb(Enum):
    SYSTEM = "SYSTEM"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def __str__(self):
        return self.value


class MessageType(Enum):
    BANK_UPDATED = "BANK_UPDATED"
    PEDALBOARD_UPDATED = "PEDALBOARD_UPDATED"
    EFFECT_UPDATED = "EFFECT_UPDATED"
    EFFECT_STATUS_TOGGLED = "EFFECT_STATUS_TOGGLED"
    PARAM_VALUE_CHANGE = "PARAM_VALUE_CHANGE"
    CONNECTION_UPDATED = "CONNECTION_UPDATED"

    def __str__(self):
        return self.value
