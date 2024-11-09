import re

s = "This is MAHA-DBT portal for Student"

# Searching for the word 'portal' in the string
match = re.search(r'portal', s)

# Checking if there is a match
if match:
    print("Start Index : ", match.start())
    print("End Index : ", match.end())
else:
    print("No match found")
