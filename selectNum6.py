import random
import tkinter
from tkinter import messagebox as msgBox

LOTTO_NUM_SIZE = 6
lottoNum = []
randonNum = 0;
msg = ""

while len(lottoNum) < LOTTO_NUM_SIZE:
    randonNum = random.randint(1,43)
    if randonNum not in lottoNum:
        lottoNum.append(randonNum)
    pass

for idx01 in range(len(lottoNum)):
    for idx02 in range(idx01+1,len(lottoNum)):
        if lottoNum[idx01] > lottoNum[idx02]:
            lottoNum[idx01] , lottoNum[idx02] = lottoNum[idx02] , lottoNum[idx01]
            pass
        pass
    pass

msg = "Lucky Num is "
for idx03 in range(len(lottoNum)):
    msg += "[" + str(lottoNum[idx03]) + "] "
    pass
msg +="\nGood Luck!!"

print(lottoNum)
msgBox.showinfo('로또번호생성기',msg)
