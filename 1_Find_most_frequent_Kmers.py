##This program is used to determine the most frequent k-mer (using k=3 as an example) in a given DNA sequence.

import itertools

def countkmers(sequence, k = 3):
    bases = ["A","T","C","G"]
    kms = [''.join(x) for x in itertools.product('ATGC', repeat=3)] ## create all possible conbinations of k-mers as a dictionary
    Possible_kmers = dict.fromkeys(kms,0)  ## assign all values as 0 in the dictionary
    for key in Possible_kmers:
        for i in range(len(sequence)-k+1):
            if sequence[i:i+k] == key:
                Possible_kmers[key] += 1
    return Possible_kmers


most = countkmers("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3)

print(most)
print type(most)   ## output will be <type 'dict'>

print(max(most,key=most.get))  ##output will be the most frequenct kmer
