#! python3

import re, pyperclip

# Get the phone numbers and emails form the copyed text and copy it to clipboard

phoneReg = re.compile(r''' 
(
((\d\d\d)|(\(\d\d\d\)))?        # 333 or (333)
-                          # -
\d\d\d                          # 333
-                          # - 
\d\d\d\d                        # 333
(((ext(\.)?\s)|x) (\d{2,5}))?   # ext. 12345 or ext 123 or x1234
)
''', re.VERBOSE)

emailReg = re.compile(r'''

[A-Za-z0-9_.+-]+        # username
@                       # literaly @                      
[A-Za-z0-9-]+           # mail service
\.                      # . separator
[A-Za-z0-9-.]+         # domain (end of line)                      
''', re.VERBOSE)

text = pyperclip.paste()
findPhone = phoneReg.findall(text)


allPhones= []

for i in findPhone:
    allPhones.append(i[0])

findMail = emailReg.findall(text)

allPhones = '\n'.join(allPhones)
allMails = '\n'.join(findMail)

print(pyperclip.copy(allPhones + '\n' + allMails))
