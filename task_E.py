# Assign the DNA sequence to a variable
dna_sequence = (
    "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT "
    "TTCTTGCTTT CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT "
    "GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT "
    "CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"
)

# Split the sequence into individual 8-character groups
sequences = dna_sequence.split()

# Reverse each 8-character sequence
reversed_sequences = [seq[::-1] for seq in sequences]

# Join the reversed sequences into a single string with spaces
reversed_dna_sequence = " ".join(reversed_sequences)

# Count the number of times "TTACT" occurs in the original sequence
ttact_count = dna_sequence.replace(" ", "").count("TTACT")

# Output the results
print("Reversed 8-length sequences:")
print(reversed_dna_sequence)

print("Count of 'TTACT' in the sequence:")
print(ttact_count)
