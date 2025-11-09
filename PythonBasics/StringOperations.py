# This program is about String Operations

str = "shivani.01magic@gmail.com"
str1 = "Quality Analyst"
str2 = "shivani"
str3 = "      Great       "

print(str[1])               # Char at position = h
print(str1[0:7])            # Range = Quality
print(str + str1)           # Concatenate strings = shivani.01magic@gmail.comQuality Analyst
print(str2 in str)          # Returns True / False, if str2 is substring of str = True
print(str.split("."))       # Break string in parts by . = ['shivani', '01magic@gmail', 'com']
print(str3.lstrip())        # Trim left space = "Great      "
print(str3.rstrip())        # Trim right space = "      Great"
