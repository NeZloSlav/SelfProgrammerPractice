# Задание: Напишите регулярное выражение, которое находит слово голландец.

import re

text = "bowbebfwbofwefo wfo wbueow  wfoweofnowibf wdendenuddw eu dedwobdbw dutch, nrferivreip, ifpepfbiewb. vnforfero."

reg_exp = re.findall("dutch", text, re.IGNORECASE)

print(reg_exp)
