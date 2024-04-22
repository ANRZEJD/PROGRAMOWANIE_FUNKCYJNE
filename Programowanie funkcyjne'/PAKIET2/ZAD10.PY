def concat_strings(*args):
   
    return ' '.join(args)


strings1 = "AB", "CD"
strings2 = "EF", "GH", "IJ", "KL"
strings3 = "MN", "OP", "ST", "UW"


result1 = concat_strings(*strings1)
result2 = concat_strings(*strings2)
result3 = concat_strings(*strings3)


print("Wynik 1:", result1)
print("Wynik 2:", result2)
print("Wynik 3:", result3)
