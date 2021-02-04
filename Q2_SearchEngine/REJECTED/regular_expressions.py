# http://docs.python.org/2/library/re.html
import re

text = 'gfgfdAAA1234ZZZuijjk'

m = re.search('AAA(.+?)ZZZ', text)
if m:
    found = m.group(1)

print(m)
print(found)
# found: 1234

# ########################### OR ########################### #
import re

text = 'gfgfdAAA1234ZZZuijjk'

try:
    found = re.search('AAA(.+?)ZZZ', text).group(1)
except AttributeError:
    # AAA, ZZZ not found in the original string
    found = '' # apply your error handling

# found: 1234