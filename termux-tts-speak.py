#!/usr/bin/python
import time as t
import os

while True:
    #os.system("echo Hello")
    os.system("termux-tts-speak $(date +%A\ %_I/%m\ %d/%m/%Y)")
    t.sleep(20)
