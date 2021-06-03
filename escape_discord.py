LONGEST_KEY = 3

START = "STRO*EBG"
START_WITHOUT_OUTER = "STRO*EBGZ"
ESCAPE = "SKAEP"
STAR = "STAR"

def lookup(key):
    if len(key) < 1:
        raise KeyError

    if key[0] not in (START, START_WITHOUT_OUTER):
        raise KeyError

    outer = "" if key[0] == START_WITHOUT_OUTER else "`"

    if len(key) == 1:
        return outer + "reading stroke..."

    if key[1] == ESCAPE:
        if len(key) != 3:
            return outer + "escaping..."

        if key[2] == "*":
            raise KeyError
        elif key[2] == STAR:
            output = "*"
        else:
            output = key[2]
    else:
        if len(key) != 2:
            raise KeyError

        output = key[1]

    return outer + output + outer