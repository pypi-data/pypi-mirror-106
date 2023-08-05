import sys
from pynput.keyboard import Key, Controller

def set(revision):
    file = open(revision, 'r')
    lines = file.readlines()

    for line in lines:
        print(line)
