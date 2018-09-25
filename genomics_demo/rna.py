#from dna import DNA

complementary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


class RNA:
    def __init__(self, sequence: str):  # type notation works only in python 3
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain A, U, C, and G.")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence={})".format(self.sequence)

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
    def complement(self):
        return RNA(''.join(complementary_nucleotides[nucleotide.upper()] for nucleotide in self.sequence))

    # def reverse_transcribe(self):
    #     # return DNA(str(self.complement).replace('U', 'T'))
    #     return str(self.complement).replace('U', 'T')
