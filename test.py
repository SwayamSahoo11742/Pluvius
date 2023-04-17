from Scopul import Scopul, config_musescore
from music21 import environment, converter
import os


def last_id():
    try:
        id = os.listdir("reports")[-1]
    except:
        id = 0

    return int(id) + 1


print(last_id())
