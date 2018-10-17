#!/usr/bin/env python3

def remove_comments(filename):
    f = open('filename')
    text = f.read()
    while text.index('#') != -1:
