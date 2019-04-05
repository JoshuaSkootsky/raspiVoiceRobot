import urllib.request
import re
f = urllib.request.urlopen("https://commodity.com/debt-clock/")
pattern = re.compile(r'.*?.png\" alt=\"([A-Za-z ]+)\".*?strong>\$([0-9,]+)')
data = f.read().decode()
f = open("text.txt","w")
found = re.findall(pattern,data)
for name in found:
    f.write(name+'\n')