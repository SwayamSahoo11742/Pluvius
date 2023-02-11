from music21 import converter, meter, tempo
from mido import bpm2tempo, tempo2bpm 
class Tempo:
    def __init__(self, midi : str):
        self._midi = converter.parse(midi)
        self._bpm_list = get_tempos(self._midi)
        self._midi_tempo_list = [bpm2tempo(m) for m in self.bpm_list]
    
    @property
    def bpm_list(self):
        return self._bpm_list

    @property
    def midi_tempo_list(self):
        return self._midi_tempo_list
    
    @classmethod
    def midi_tempo2bpm(self, tempo: int | list) -> float | list:
        try:
            if type(tempo) == int:
                return tempo2bpm(tempo)
            elif type(tempo) == list:
                return [tempo2bpm(m) for m in tempo]
        except TypeError:
            raise TypeError("midi_tempo2bpm only accepts str or list objects")
    
    @classmethod
    def bpm2midi_tempo(self, tempo: int | list) -> float | list:
        try:
            if type(tempo) == int:
                return bpm2tempo(tempo)
            elif type(tempo) == list:
                return [bpm2tempo(m) for m in tempo]
        except TypeError:
            raise TypeError("bpm2midi_tempo only accepts str or list objects")
    



def get_tempos(midi):
    lst = []
    for i in midi.flat:
        if isinstance(i, tempo.MetronomeMark):
            lst.append(i.number)
    
    return lst
