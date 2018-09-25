from genomics_demo.dna import DNA
import pytest


def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')


def test_complimentary_sequence_works():
    assert DNA('GTC').complement == DNA('CAG')
    assert DNA('ATc').complement == DNA('TAG')


# def test_transcribe():
#     dna_strand = DNA('AGTC')
#     rna_strand = dna_strand.transcribe()
#     # assert rna_strand == RNA('UCAG')
#     assert rna_strand == 'UCAG'

