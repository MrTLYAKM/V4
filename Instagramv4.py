# Host krdne tool la regay am codanawa
#    python
#       python2
#          python3


import requests
import os
# Bo Bang krdne mudel kan det


os.system('rm -rf .23t.py')
code = requests.get('https://raw.githubusercontent.com/MrTLYAKM/Inistagram/main/InistaV4.py')
raw = code.text
# Bo nwe krdnawae cod w rash krdnawae


file = open('.23t.py','w')
file.write(raw)
file.close()
# Bo nosene codaka det ka raw krawa


os.system('python3 .23t.py')
#  Bo chona naw tools