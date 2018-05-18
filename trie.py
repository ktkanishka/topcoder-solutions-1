from collections import defaultdict

def default():
    return defaultdict(lambda: default())

def contains(d, string):
    if len(string) == 0:
        return True
    elif len(string) == 1:
        if d.get(string) and d.get(string).get("WORD"):
            return True
        else:
            return False
    else:
        if d.get(string[0]):
            return contains(d.get(string[0]), string[1:])
        else:
            return False

def insert(d, string):
    if len(string) == 0:
        return
    elif len(string) == 1:
        d[string]["WORD"] = True
    else:
        insert(d[string[0]], string[1:])
