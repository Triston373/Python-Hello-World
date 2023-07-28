multi_line_sentence = """ 
The triple quotes are used for multi-line strings!
They are also used to escape quotation marks, if needed.
"""
simple_sentence = "Hello World! It's a great day!"

# Printing a character of a string, which can be indexed like an array!
print(simple_sentence[0])
# A colon can be used within brackets to select and print characters between a range.
print(simple_sentence[:5])
print(simple_sentence[5:])
print(simple_sentence[2:8])
print(simple_sentence[:])
# Negative character indexes work too. They start indexing form the back of the string.
print(simple_sentence[1:-2])

# Strings can be formatted. Prefix the string with an 'f' and use {}
print(f'Here is a sentence: {simple_sentence} That is the end!')

# Functions create new strings that modify string case
print(simple_sentence.upper())
print(simple_sentence.lower())

# Function returns index of first occurrence of parameter in string.
print(simple_sentence.find('!'))
# Function finds and replaces string
print(simple_sentence.replace('World', 'Continent'))

# 'in' operator creates boolean if string is within another string
print('World' in simple_sentence)


