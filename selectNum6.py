import random
import tkinter
from tkinter import messagebox as msgBox
from flask import Flask

LOTTO_NUM_SIZE = 6
lottoNum = []
randonNum = 0;
msg = ""

def makeNum():
    while len(lottoNum) < LOTTO_NUM_SIZE:
        randonNum = random.randint(1,43)
        if randonNum not in lottoNum:
            lottoNum.append(randonNum)
    bubSort(lottoNum)
    writeMsg(lottoNum)
    return lottoNum

def bubSort(lottoNum):
    for idx01 in range(len(lottoNum)):
        for idx02 in range(idx01+1,len(lottoNum)):
            if lottoNum[idx01] > lottoNum[idx02]:
                lottoNum[idx01] , lottoNum[idx02] = lottoNum[idx02] , lottoNum[idx01]
    return lottoNum

def writeMsg(lottoNum):
    msg = "Lucky Num is\n"
    for idx03 in range(len(lottoNum)):
        msg += "[" + str(lottoNum[idx03]) + "] "
    msg +="\nGood Luck!!"
    print(msg)
    return msg

makeNum()


# app = Flask(__name__)
#
# @app.route('/')
# def hello():
# 	return msg
#
# if __name__ == '__main__':
# 	app.run(debug=True)
# msgBox.showinfo('lotto6',msg)
