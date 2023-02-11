from music21 import meter, converter


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
    def count(self) -> int:
        """Get the count of the number of time signatures.

        Returns:
            An Integer representing the count of time signature appearances
            Example:

            test_midi.count = 2
        
        """
        # initiate counter
        count = 0

        for i in self.midi.flat:
            # Check if the element is a TimeSignature object
            if isinstance(i, meter.TimeSignature):
                count += 1

        return count

    # Time Signature appearances list (list)
    @property
    def list(self, unique : bool = False) -> list | set:
        """Fetches every occurance of a time signature.
                   
            Retrieves all the occurances of time signatures, with an optional ability to get unique signatures only.

            Args:
                unique: Optional boolean value to indicate whether to return unique time changes or to repeat
            
            Returns:
                A list or set object with time signatures in it.
            
                
        """
        # List of signatures
        sig_list = []

        for i in self.midi.flat:
            # Check if the element is a TimeSignature object
            if isinstance(i, meter.TimeSignature):
                # Appending to list
                sig_list.append(i.ratioString)

        if unique:
            return set(sig_list)
        else:
            return sig_list

    # Str method
    def __str__(self):
        return self.ratio
