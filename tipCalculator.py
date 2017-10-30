#!/usr/bin/env python
#
# Input:
# bill amount
# tip rate
#
# expected result:
# tip
# total

tipRate = input("Enter the tip rate: ");
billAmount = input("Enter the bill amount: ");

tip = ((tipRate / 100.00) * billAmount);
total = (tip + billAmount);

print ("The tip amount is " + str(tip));
print ("The total amount is " + str(total));
