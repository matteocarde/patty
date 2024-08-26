import sys
import traceback


class ValidationError(Exception):

    def __init__(self, message):
        print(message, file=sys.stderr)
        pass


class ValAssert:

    def __init__(self, assertion: bool, messageIfNotAsserted: str):
        if assertion:
            return
        traceback.print_exc()
        raise ValidationError(messageIfNotAsserted)
