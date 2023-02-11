from music21 import converter, environment

# Setting up music21 with MuseScore
env = environment.Environment()
env["musicxmlPath"] = r"MuseScore 4/bin/MuseScore4.exe"
env["musescoreDirectPNGPath"] = r"MuseScore 4/bin/MuseScore4.exe"

from TimeSignature import TimeSignature
from Tempo import Tempo


class Scopul(Tempo):
    def __init__(self, audio):
        self.construct(audio)

    # Tempo (tempo)
    @property
    def tempo(self):
        """Fetches Tempo object"""
        return self._tempo

    # Time Signature (time_sig)
    @property
    def time_sig(self):
        """Fetches the Time Signature object"""
        return self._time_sig

    # Midi File (midi)
    @property
    def midi(self):
        """Retrieves your midi file."""
        return self._midi

    # Midi File setter
    @midi.setter
    def midi(self, audio):
        """Allows to reconstruct the object to change accordingly to a new midi"""
        self.construct(audio)

    # (Re)constructor
    def construct(self, audio):
        """Constructor function to reconstruct the object

        Can also be called with a setter to the midi attribute. For example:

        testmidi.midi = "test.mid"

        """
        self._midi = converter.parse(audio)
        self._time_sig = TimeSignature(audio)
        self._tempo = Tempo(audio)


