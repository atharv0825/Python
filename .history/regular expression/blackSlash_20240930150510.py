import re

s = "Atharv.Babar"

match = re.search(r'.',s)
print('Withiot',match)
match = re.search(r'\.',s)
print("With using",match)