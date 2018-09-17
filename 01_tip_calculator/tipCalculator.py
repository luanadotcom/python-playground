#!/usr/bin/env python
#
# Input:
# bill amount
# tip rate
#
# expected result:
# tip
# total
import numbers

def billValues ():
    tipRate = int(input("Enter the tip rate: "))
    billAmount = int(input("Enter the bill amount: "))
    return(tipRate, billAmount)

def calculateValues (tipRate, billAmount):
    tip = ((tipRate / 100.00) * billAmount)
    total = (tip + billAmount)
    return(tip,total)

while True:
    tipRate, billAmount = billValues()
    if isinstance(tipRate, int) and isinstance(billAmount, int):
        calculateValues(tipRate, billAmount)
        print ("The tip amount is %s" % (tip))
        print ("The total amount is %s" % (total))
        break
    else:
        print("Error: Please only enter numbers as tip rate and bill amount")
