import json

def load_books():
    try:
        file = open("library.json")
        return json.load(file)
    except:
        return []


def load_records():
    try:
        file = open("records.json")
        return json.load(file)
    except:
        return []