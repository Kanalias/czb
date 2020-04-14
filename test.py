


import json

import pymorphy2
from pymystem3 import Mystem
morph = pymorphy2.MorphAnalyzer()
print(morph.parse("будет"))

text = "умнее"
m = Mystem()
a = m.analyze(text)[0]
print(a)
if "прич" in a["analysis"][0]["gr"]:
    print(a)