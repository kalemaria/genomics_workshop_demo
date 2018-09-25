from dna import DNA

try:
    assert DNA('ATB')
except ValueError:
    pass
assert DNA('GTC').complementary_sequence == DNA('CAG')
assert DNA('ATc').complementary_sequence == DNA('TAG')
dna = DNA('ACT')

print('it worked!')
