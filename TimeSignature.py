from music21 import meter, stream, converter, environment


class TimeSignature:
    def __init__(self, audio):
        self.midi = converter.parse(audio)
        self._ratio = f"{self.midi[meter.TimeSignature][0].numerator}/{self.midi[meter.TimeSignature][0].denominator}"
        self._numerator = int(self.ratio.split("/")[0])
        self._denominator = int(self.ratio.split("/")[1])

    # Signature denominator (denominator)
    @property
    def denominator(self):
        return self._denominator

    # Signature numerator (numerator)
    @property
    def numerator(self):
        return self._numerator

    # Signature Ratio (ratio)
    @property
    def ratio(self):
        return self._ratio

    # Time Signature appearance count (count)
    @property
    def count(self):
        """Get the count of the number of time signatures"""
        # initiate counter
        count = 0

        for i in self.midi.flat:
            # Check if the element is a TimeSignature object
            if isinstance(i, meter.TimeSignature):
                count += 1

        return count

    # Time Signature appearances list (list)
    @property
    def list(self):
        # List of signatures
        sig_list = []

        for i in self.midi.flat:
            # Check if the element is a TimeSignature object
            if isinstance(i, meter.TimeSignature):
                # Appending to list
                sig_list.append(i.ratioString)

        return sig_list

    # Str method
    def __str__(self):
        return self.ratio
