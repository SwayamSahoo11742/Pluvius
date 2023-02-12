from music21 import converter, environment, instrument

# Setting up music21 with MuseScore
env = environment.Environment()
env["musicxmlPath"] = r"MuseScore 4/bin/MuseScore4.exe"
env["musescoreDirectPNGPath"] = r"MuseScore 4/bin/MuseScore4.exe"

from TimeSignature import TimeSignature
from Tempo import Tempo
from Sequence import Part, Rest, Chord, Note


class Scopul(Tempo):
    def __init__(self, audio):
        self.construct(audio)

    # Tempo (tempo)
    @property
    def tempo(self) -> Tempo:
        """Fetches Tempo object"""
        return self._tempo

    # Time Signature (time_sig)
    @property
    def time_sig(self) -> TimeSignature:
        """Fetches the Time Signature object"""
        return self._time_sig

    # Midi File (midi)
    @property
    def midi(self):
        """Retrieves your midi file."""
        return self._midi
    
    @property
    def parts(self):
        """Retrieves a list of Part objects

            Example:
                [Part Object 1, Part Object 2]
        """
        return self._parts

    # Midi File setter
    @midi.setter
    def midi(self, audio) -> None:
        """Allows to reconstruct the object to change accordingly to a new midi"""
        self.construct(audio)

    # (Re)constructor
    def construct(self, audio) -> None:
        """Constructor function to reconstruct the object

        Can also be called with a setter to the midi attribute. For example:

        testmidi.midi = "test.mid"

        """
        self._midi = converter.parse(audio)
        self._time_sig = TimeSignature(audio)
        self._tempo = Tempo(audio)
        self._parts = []
        for part in self.midi.parts:
            self._parts.append(Part(part))


mid = Scopul("testfiles/test1.mid")

for idx, i in enumerate(mid.parts[0].sequence):
    if idx == 412:
        print(type(i))
        print(i.measure)
        print([n.name for n in i.notes])
        print(i.lenght)

