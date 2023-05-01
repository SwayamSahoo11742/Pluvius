from Scopul import Scopul, config_musescore, Note
from copy import deepcopy
from music21 import (
    environment,
    converter,
    musicxml,
    stream,
    note,
    chord,
    metadata,
    percussion,
    meter,
    instrument,
    key,
    clef,
    bar,
    tempo,
)
import os

env = environment.Environment()
environment.set("debug", False)

config_musescore(
    "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"
)
env[
    "musicxmlPath"
] = "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"
env[
    "musescoreDirectPNGPath"
] = "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"

input_file = "testfiles/test3.mid"
output_file = "help.pdf"

scop = Scopul(input_file)

scop.add_note(Note(name="C5", length=6), scop.parts[0], 2)
scop.save_midi("wierd.mid", overwrite=True)
