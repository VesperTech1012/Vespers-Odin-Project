def get_dna_sequence(prompt):
    while True:
        sequence = input(prompt).upper()
        if len(sequence) >= 10 and all(nuc in 'ACTG' for nuc in sequence):
            return ['O'] + list(sequence)
        else:
            print("Invalid input. Please enter a DNA sequence of at least 10 nucleotides (A, C, T, G).")

list1 = get_dna_sequence("Enter the first DNA sequence: ")
list2 = get_dna_sequence("Enter the second DNA sequence: ")

table = list(zip(list1, list2))

for item1, item2 in table:
    print(f"{item1} -> {item2}")
