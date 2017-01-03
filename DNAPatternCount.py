# Copy your PatternCount function from the previous step below this line
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
Pattern = "AAA"

# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
print(PatternCount(Pattern, Text))
