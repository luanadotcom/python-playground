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

tipRate = float(raw_input("Enter the tip rate: "));
while not isinstance(tipRate, int):
    tipRate = input("Please only enter numbers as the tip rate: ");

billAmount = raw_input("Enter the bill amount: ");
while not isinstance(billAmount, float) or isinstance(billAmount, int):
    billAmount = input("Please only enter number as the bill amount: ")

tip = ((tipRate / 100.00) * billAmount);
total = (tip + billAmount);

print ("The tip amount is " + str(tip));
print ("The total amount is " + str(total));
