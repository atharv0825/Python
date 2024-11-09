import re

s = "This is MAHA-DBT portal for Student"

match = re.search(r'portal',s);

print("Start Index : ",match.start())
print("End Index : ",match.end())