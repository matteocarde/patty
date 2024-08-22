import sys
import traceback


class ValidationError(Exception):

    def __init__(self, message):
        traceback.print_exc()
        print(message, file=sys.stderr)
        pass


class ValAssert:

    def __init__(self, assertion: bool, messageIfNotAsserted: str):
        if assertion:
            return

        raise ValidationError(messageIfNotAsserted)
