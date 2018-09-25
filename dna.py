complimentary_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


class DNA:
    def __init__(self, sequence: str):  # type notation works only in python 3
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain A, T, C, and G.")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "DNA(sequence={})".format(self.sequence)

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAT' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
    def complementary_sequence(self):
        return DNA(''.join(complimentary_nucleotides[nucleotide.upper()] for nucleotide in self.sequence))


if __name__ == '__main__':
    try:
        assert DNA('ATB')
    except ValueError:
        pass
    assert DNA('GTC').complementary_sequence == DNA('CAG')
    assert DNA('ATc').complementary_sequence == DNA('TAG')
    dna = DNA('ACT')

    print('it worked!')
