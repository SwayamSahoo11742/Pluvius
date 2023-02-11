from conversions import number_to_note
from scopul import Scopul
from music21 import environment, configure, converter, meter
import os


def main():
    scop = Scopul("testfiles/test3.mid")
    save_pdf("testfiles/test3.mid")


def get_tempo(midi):
    for track in midi:
        if track.is_meta:
            try:
                return track.tempo
            except AttributeError:
                pass


def get_time_signature(midi):
    sig_list = []
    midi = converter.parse(midi)
    for i in midi.flat:
        # Check if the element is a TimeSignature object
        if isinstance(i, meter.TimeSignature):
            sig_list.append(i.ratioString)
    return sig_list


def get_note_sequence(midi):
    seq = []
    for track in midi:
        if not track.is_meta:
            try:
                note_data = {"note": number_to_note(track.note), "time": track.time}
                if track.type == "note_on":
                    note_data["type"] = "note_on"
                else:
                    note_data["type"] = "note_off"
                seq.append(note_data)
            except AttributeError:
                pass
    return seq


def save_pdf(midi):
    score = converter.parse(midi)
    # score.write("musicxml.pdf", fp="", filename="hello.pdf")
    score.show()


if __name__ == "__main__":
    main()
