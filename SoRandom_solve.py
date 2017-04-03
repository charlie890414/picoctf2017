#!/usr/bin/python -u
import random,string
encflag="BNZQ:1o0yd5jk9h256wdjsu366t10787198h9"
flag=""
random.seed("random")
for c in encflag:
  if c.islower():
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
  else:
    flag += c
print flag
