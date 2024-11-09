import RE
import re

match = re.search(r'portal', REs)


if match:
    print("Start Index : ", match.start())
    print("End Index : ", match.end())
else:
    print("No match found")