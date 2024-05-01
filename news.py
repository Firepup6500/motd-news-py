#!/usr/bin/python
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve as curl

doc = ET.parse(curl("https://micronews.debian.org/feeds/atom.xml")[0]).getroot()
drops = {}
drops[0] = doc[5][0].text
while any(len(drops[i]) > 77 for i in drops.keys()):
    ind = -1
    g = False
    for j in drops.keys():
        ind += 1
        if len(drops[j]) > 77:
            if len(drops[j].split()) > 1:
                g = True
                break
            else:
                drops[j] = drops[j][:74] + "..."
    if not g:
        break
    if drops.get(ind + 1, None) == None:
        drops[ind + 1] = ""
    drops[ind + 1] = f"{drops[ind].split()[-1]} {drops[ind+1]}".strip()
    drops[ind] = " ".join(drops[ind].split()[:-1])
title = "\n * ".join(drops.values()).lstrip("\n")
link = doc[5][1].attrib["href"]
print(
    f""" * {title}

   {link}"""
)
