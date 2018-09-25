from rna import RNA
import pytest


def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('AUB')


def test_complimentary_sequence_works():
    assert RNA('AGUC').complement == RNA('UCAG')


# def test_reverse_transcribe():
#     rna_strand = RNA('AGUC')
#     dna_strand = rna_strand.reverse_transcribe()
#     # assert dna_strand == DNA('TCAG')
#     assert dna_strand == 'TCAG'
