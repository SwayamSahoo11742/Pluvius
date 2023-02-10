from music21 import converter, environment

# Setting up music21 with MuseScore
env = environment.Environment()
env["musicxmlPath"] = r"MuseScore 4/bin/MuseScore4.exe"
env["musescoreDirectPNGPath"] = r"MuseScore 4/bin/MuseScore4.exe"

from TimeSignature import TimeSignature


class Scopul:
    def __init__(self, audio):
        self.construct(audio)

    # Time Signature (time_sig)
    @property
    def time_sig(self):
        return self._time_sig

    # Midi File (midi)
    @property
    def midi(self):
        return self._midi

    # Midi File setter
    @midi.setter
    def midi(self, audio):
        self.construct(audio)

    # (Re)constructor
    def construct(self, audio):
        self._midi = converter.parse(audio)
        self._time_sig = TimeSignature(audio)
