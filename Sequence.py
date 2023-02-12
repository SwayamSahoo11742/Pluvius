from music21 import meter, converter, instrument, stream, note, chord


class Part:
    """A class representing the a part in a score.
    EX: A flute part
    """

    def __init__(self, part) -> None:
        self.part = part
        self.name = part.partName
        self.sequence = []
        # Looping through the part
        for element in part.recurse():
            # Setting the class and appending depending on the type of symbol
            if isinstance(element, note.Note):
                self.sequence.append(Note(element))
            elif isinstance(element, chord.Chord):
                self.sequence.append(Chord(element))
            elif isinstance(element, note.Rest):
                self.sequence.append(Rest(element))

    def get_measure(self, m: int | list):
        """Fetches the contents of a measure.

        Retrieves about chords, notes and rest objects in the sequence

        Args:
            m: an int, representing the measure or a list [start, end], representing a range of measures

        Returns:
            A list with all the contents in the measure(s) requested

        Raises:
            ValueError: if inputted negative number, or a list with not lenght of 2
            TypeError: if input is not a list of int
        """
        # If integer
        if type(m) == int:

            # if invalid integer
            if m <= 0:
                raise ValueError("get_measure only allows positive integers")

            seq = []
            for i in self.sequence:
                if i.measure == m:
                    seq.append(i)
            return seq

        # If list
        elif type(m) == list:

            # Check for positive int
            for i in m:
                if i <= 0:
                    raise ValueError("get_measure only allows positive integers")

            # check for only start and end values
            if len(m) != 2:
                raise ValueError("usage: get_measure([start, end])")

            seq = []
            for i in self.sequence:
                if i.measure in range(m[0], m[1] + 1):
                    seq.append(i)
            return seq

        # Incorrect type
        else:
            raise TypeError(
                f"get_measure only accepts int or list, instead got {type(m)}"
            )


class Note:
    """A Class for all the notes"""

    def __init__(self, note) -> None:
        self._name = note.pitch.nameWithOctave
        self._measure = note.measureNumber
        self._velocity = note.volume.velocity
        self._lenght = note.duration.type

    @property
    def name(self):
        """Returns the note in 'letter-name octave' format.

        Example:
            C4
            D5
            B-4
        """
        return self._name

    @property
    def measure(self):
        """Returns an int representing the measure"""
        return self._measure

    @property
    def velocity(self):
        """Returns an int, representing velocity of the note"""
        self._velocity

    @property
    def lenght(self):
        """Returns a str representing the lenght of the note

        Example:
            "quarter"

        """
        return self._lenght


class Rest:
    """A Class for all the rests"""

    def __init__(self, rest) -> None:
        self._measure = rest.measureNumber
        self._lenght = rest.duration.type

    @property
    def lenght(self):
        """Returns a str, indicating the lenght of the rest

        Example:
            "whole"
        """
        return self._lenght

    @property
    def measure(self):
        """Returns an int, representing the measure number"""
        return self._measure


class Chord:
    """A Class to represent a chord (multiple notes at once)"""
    def __init__(self, chord) -> None:
        # Converting to notes
        self._notes = [Note(n) for n in list(chord.notes)]
        self._measure = chord.measureNumber
        self._lenght = chord.duration.type
    
    @property
    def lenght(self):
        """Returns a str, representing the lenght of the chord

        Example:
            "eighth"
        """
        return self._lenght

    @property
    def measure(self):
        """Returns an int, representing the measure number"""
        return self._measure

    @property
    def notes(self):
        """Retrieves a list of notes in a chord

            Returns;
                A list, consisting of Note objects. For example:

                [Note Object, Note Object]
        """
        return self._notes

print()