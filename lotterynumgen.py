"""
Python Final - Stephanie Kordulak | 5/1/2020
"""
import random
from breezypythongui import EasyFrame


class LotteryNumGen(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Lottery Number Generator", width= 350, height = 200)

        # create/add widgets to window
        self.addLabel(text="Lottery Number Generator", row=0, column=0)
        self.numField1 = self.addLabel(text="", row=2, column=1)
        self.numField2 = self.addLabel(text="", row=2, column=2)
        self.numField3 = self.addLabel(text="", row=2, column=3)
        self.numField4 = self.addLabel(text="", row=2, column=4)
        self.numField5 = self.addLabel(text="", row=2, column=5)
        self.pbField = self.addLabel(text="", row=2, column=6)

        # button
        self.addButton(text="Play!", row=5, column=0, command = self.playGame)

    def playGame(self):
        # generate random lotto numbers
        self.numField1["text"] = random.randint(1, 69)
        self.numField2["text"] = random.randint(1, 69)
        self.numField3["text"] = random.randint(1, 69)
        self.numField4["text"] = random.randint(1, 69)
        self.numField5["text"] = random.randint(1, 69)
        self.pbField["text"] = random.randint(1, 26)

def main():
    LotteryNumGen().mainloop()

main()