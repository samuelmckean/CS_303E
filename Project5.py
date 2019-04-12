# Compares two dna strands to return the longest match using recursion
def dnaCompare(s1, s2):
    # If match return s1 and s2
    match = True    # Indicates whether strand was match
    firstNonMatchIndex = 0  # Index of first unmatched letters
    # Loop through all chars and check for match
    for i in range(len(s1)):
        # If match check next char
        if (s1[i] == 'A' and s2[i] == 'T' or
                s1[i] == 'T' and s2[i] == 'A' or
                s1[i] == 'C' and s2[i] == 'G' or
                s1[i] == 'G' and s2[i] == 'C'):
            continue
        # If not match, update firstNonMatchIndex and match
        else:
            firstNonMatchIndex = i
            match = False
            break
    if match:
        return s1, s2
    # Create new strands excluding firstNonMatch and recall dnaCompare
    else:
        # Separate strands at firstNonMatch index (excluding index itself)
        s11, s12 = dnaCompare(s1[:firstNonMatchIndex], s2[:firstNonMatchIndex])
        s21, s22 = dnaCompare(s1[firstNonMatchIndex+1:], s2[firstNonMatchIndex+1:])

        # Return larger strand of pairs
        if len(s11) > len(s21):
            return s11, s12
        else:
            return s21, s22


def main():
    # Open dna.txt as read-only
    inFile = open("dna.txt", 'r')

    # Open dnaresults as write-only
    outFile = open("dnaresults.txt", 'w')

    # Read in number of pairs
    pairs = int(inFile.readline().strip())

    # Loop through pairs and compare
    for i in range(pairs):
        # Read in strands from inFile
        dna1 = inFile.readline().strip().upper()
        dna2 = inFile.readline().strip().upper()
        match1, match2 = dnaCompare(dna1, dna2)

        # Write results to outFile
        outFile.write("DNA sequence pair {}:\n".format(i))
        # Write pairs if match found
        if len(match1) > 1:
            outFile.write(match1 + '\n')
            outFile.write(match2 + '\n\n')
        # Write No matches found
        else:
            outFile.write("No matches found\n\n")

    # Close files
    inFile.close()
    outFile.close()


main()
