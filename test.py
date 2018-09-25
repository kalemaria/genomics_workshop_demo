from dna import DNA
import pytest


def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')


def test_complimentary_sequence_works():
    assert DNA('GTC').complementary_sequence == DNA('CAG')
    assert DNA('ATc').complementary_sequence == DNA('TAG')
