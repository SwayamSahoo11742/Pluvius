from conversions import number_to_note, note_to_number
from scopul import Scopul



def main():
    scop = Scopul("testfiles/test1.mid")
    scop.generate_pdf("hello.pdf", overwrite=True)


if __name__ == "__main__":
    main()
