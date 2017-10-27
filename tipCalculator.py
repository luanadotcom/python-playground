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

tip = str(((tipRate / 100) * billAmount));
total = str((tip + billAmount));

print ("The tip amount is " + tip);
print ("The total amount is " + total);

