import io
class Data():
    quLength = 15
    img = ''
    # Queue with 15 items
    inc1 = {"Temp":[[],[]], "Humid":[[],[]],
            "Lum": [[], []]}
    inc2 = {"Temp": [[], []], "Humid": [[], []],
            "Lum": [[], []]}
    inc3 = {"Temp": [[], []], "Humid": [[], []],
            "Lum": [[], []]}
    inc4 = {"Temp": [[], []], "Humid": [[], []],
            "Lum": [[], []]}

    def updateData(self, jData):
        if jData["incID"] == 1:
            if len(self.inc1["Temp"][1]) == self.quLength:
                del self.inc1["Temp"][1][0]
                del self.inc1["Humid"][1][0]
                del self.inc1["Lum"][1][0]
            else:
                inc1Num = int(len(self.inc1["Temp"][0]) + 1)
                self.inc1["Temp"][0].append(inc1Num)
                self.inc1["Humid"][0].append(inc1Num)
                self.inc1["Lum"][0].append(inc1Num)

            self.inc1["Temp"][1].append(int(jData["Temp"]))
            self.inc1["Humid"][1].append(int(jData["Humid"]))
            self.inc1["Lum"][1].append(int(jData["Lum"]))

        # elif data["incID"] == 2:
        #     if len(self.inc2["Temp"][1]) == self.quLength:
        #         del self.inc2["Temp"][1][0] , self.inc2["Humid"][1][0], self.inc2["Lum"][1][0]
        #     else:
        #         inc1Num = len(self.inc1["Temp"][0]) + 1
        #         self.inc1["Temp"][0].append(inc1Num) , self.inc1["Humid"][0].append(inc1Num)
        #         self.inc1["Lum"].append(inc1Num)
        #     self.inc2["Temp"][1].append(data["temp"])
        #     self.inc2["Humid"][1].append(data["humid"]), self.inc2["Lum"][1].append(data["lum"])
        # elif data["incID"] == 3:
        #     if len(self.inc3["Temp"][1]) == self.quLength:
        #         del self.inc3["Temp"][1][0] , self.inc3["Humid"][1][0], self.inc3["Lum"][1][0]
        #     else:
        #         inc1Num = len(self.inc1["Temp"][0]) + 1
        #         self.inc1["Temp"][0].append(inc1Num) , self.inc1["Humid"][0].append(inc1Num)
        #         self.inc1["Lum"].append(inc1Num)
        #     self.inc3["Temp"][1].append(data["temp"])
        #     self.inc3["Humid"][1].append(data["humid"]), self.inc3["Lum"][1].append(data["lum"])
        # elif data["incID"] == 4:
        #     if len(self.inc4["Temp"][1]) == self.quLength:
        #         del self.inc4["Temp"][1][0] , self.inc4["Humid"][1][0], self.inc4["Lum"][1][0]
        #     else:
        #         inc1Num = len(self.inc1["Temp"][0]) + 1
        #         self.inc1["Temp"][0].append(inc1Num) , self.inc1["Humid"][0].append(inc1Num)
        #         self.inc1["Lum"].append(inc1Num)
        #     self.inc4["Temp"][1].append(data["temp"])
        #     self.inc4["Humid"][1].append(data["humid"]), self.inc4["Lum"][1].append(data["lum"])

    ##---------------------------------------------------
