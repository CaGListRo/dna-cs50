import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python process_csv.py <database> <sequence>")
    else:
        database = sys.argv[1]
        sequence = sys.argv[2]

    # Read database file into a variable
    database_list = []
    with open(database, 'r') as dbfile:
        reader = csv.DictReader(dbfile)
        for row in reader:
            database_list.append(row)

    
    # Read DNA sequence file into a variable
    with open(sequence, 'r') as seqfile:
        dna_seq = seqfile.read().strip()
    

    # Find longest match of each STR in DNA sequence
    found = False
    for row in database_list:
        matches = 0
        keys = row.keys()
        for key in keys:
            if key != "name":
                longest_run = longest_match(dna_seq, key)
                if longest_run == int(row[key]):
                    matches += 1
                    if matches == len(keys) - 1:
                        found = True
                        print(row["name"])
    if not found:
        print(f"No matches found for {sequence}")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
