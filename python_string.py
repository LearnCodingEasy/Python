# 💻 Python 🐍 [ String ]

# PY How to write texts using three methods?
dataString = "Hello World"
dataString = 'Hello World'
dataStringStr = str("Hello World")

# PY Printing texts
print(f"Print String : {dataString}")
print(f"Print String Str() : {dataStringStr}")

# PY Knowing the type of text data
print(f"Data Type : {type(dataString)}")
print(f"Data Type Str : {type(dataStringStr)}")

# PY Find out the number of letters in texts
print(f"String Length : {len(dataString)}")

# PY Extract a specific character from texts
print(f"Index : {dataString[0]}")

# PY Extract a slice of texts
print(f"Slicing[0:6] : {dataString[0:6]}")
print(f"Slicing[:6] : {dataString[:6]}")
print(f"Slicing[5:] : {dataString[5:]}")
print(f"Slicing[:] : {dataString[:]}")

# PY Remove extra spaces from texts
print(f"Strip : {dataString.strip()}")
print(f"RStrip : {dataString.rstrip()}")
print(f"LStrip : {dataString.lstrip()}")

# PY Convert text to title case or capitalize
print(f"Title : {dataString.title()}")
print(f"Capitalize : {dataString.capitalize()}")

# PY Convert text to uppercase
print(f"Upper : {dataString.upper()}")

# PY Convert text to lowercase
print(f"Lower : {dataString.lower()}")

# PY Split text into a list
print(f"Split : {dataString.split()}")
print(f"Split : {dataString.split(' ')}")

# PY Join a list of strings
dataArray = ["Python", "is", "awesome"]
print(f"Join : {' '.join(dataArray)}")

# PY Center align text with padding
print(f"Center : {dataString.center(15)}")
print(f"Center : {dataString.center(15, '#')}")

# PY Justify text to the right or left
print(f"RJust : {dataString.rjust(15)}")
print(f"LJust : {dataString.ljust(15)}")

# PY Count occurrences of a substring
print(f"Count : {dataString.count('World')}")

# PY Find position of a substring
print(f"Find : {dataString.find('World')}")

# PY Replace a substring
print(f"Replace : {dataString.replace('World', 'Python')}")

# PY Check if text starts with a substring
print(f"Startswith : {dataString.startswith('H')}")

# PY Check if text ends with a substring
print(f"Endswith : {dataString.endswith('d')}")

# PY Check if text is numeric, alphabetic, or alphanumeric
print(f"IsDigit : {dataString.isdigit()}")
print(f"IsAlpha : {dataString.isalpha()}")
print(f"IsAlnum : {dataString.isalnum()}")

# PY Check if text contains only spaces
print(f"IsSpace : {dataString.isspace()}")

# PY Convert character to Unicode and vice versa
print(f"Ord : {ord('A')}")
print(f"Chr : {chr(65)}")

# PY Swap case of text
print(f"Swapcase : {dataString.swapcase()}")

# PY Add leading zeros to text
print(f"ZFill : {dataString.zfill(15)}")
