#!/usr/bin/python3

# Define REG. EXP. to match strings that:

# 1. Have a 't'
teste = "t a T sd - . as"
re.search(r"t",teste)

# 2. have a 't ou 'T'
re.search(r"t|T",teste)
re.search(r"[tT]",teste)
re.search(r"t",teste,re.I) # Perform case-insensitive matching.

# 3. have a letter
re.search(r"[a-z]",teste)
re.search(r"(?!=[0-9])\w",teste)

# 4. have a digit
re.search(r"[0-9]",teste)


# 5. have a decimal number
re.search(r"\d+(?:\.\d+)?",teste)

# 6. have length >3 chars
re.search(r".{4,}",teste)
re.search(r".{....+}",teste)

# 7. have an 'M' but not an 'm'
re.search(r"M" r"^[^m]+$",teste)
re.search(r"M",teste) and not r'm'

# 8. have a char repeated twice
re.search(r"(.).*\1",teste)

# 9. have only one char repeated many times
re.search(r"^(.)\1*$",teste)

# 10. put all words between { }
re.sub(r"(\w+)","{\1}",teste)
re.sub(r"([\w'-]+)","{\1}",teste)