#!/usr/bin/env python

# output:
# What is your name _Luana_
# Hello, Luana, nice to meet you!

# keep the input, string concatenation and output separate

## challenges
# write a new version of the program without using variables
# write a version of the program that displays different greetings for different people...

def gather_info():
    name = raw_input("What is your name? ")
    return(name)

def output():
    print("Hello, %s, nice to meet you" % (name))


