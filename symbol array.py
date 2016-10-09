## keep track of the total number of occurrences of C that we encounter in each window of ExtendedGenome by using a symbol array
## The i-th element of the symbol array is equal to the number of occurrences of the symbol in the window of length len(Genome)//2 starting at position i of ExtendedGenome.
''' https://stepik.org/lesson/Peculiar-Statistics-of-the-Forward-and-Reverse-Half-Strands-23059/step/8?course=Where-in-the-Genome-Does-DNA-Replication-Begin-(Part-2)&unit=6791
'''
### Sample Input:  AAAAGGGG   A

### Output is:{0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

# Reproduce the PatternCount function on the following line from Replication.py.
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(SymbolArray(lines[0],lines[1]))
