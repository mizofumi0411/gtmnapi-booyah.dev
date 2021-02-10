#!/usr/bin/env python3
import subprocess
import time
import json
import os

# /usr/bin/screen -S minecli -X stuff "list\015"

def pgrep(pattern):
    """return a list with process IDs which matches the selection criteria"""
    args = ["pgrep", str(pattern)]
    out = os.popen(" ".join(args)).read().strip()
    return out

def check(pattern):
    if (pgrep(pattern) != ''):
        return True
    else:
        return False

def read_file():
  with open('/tmp/minecli.txt', 'r') as f:
    return f.readlines()[-5:]

while True:
  subprocess.call('/usr/bin/screen -S minecli -X stuff "list\015"', shell=True)
  time.sleep(10)
  now_size = 0
  max_size = 0
  for line in read_file():
    line = line.replace('\n', '')
    print(line)
    if line == 'list' or line.startswith('['):
      continue
    if line.startswith('There are'):
      nop = line.replace('There are ','').replace('players online:','')
      now_size = nop.split('/')[0].replace(' ','')
      max_size = nop.split('/')[1].replace(' ','')
      continue
    else:
      now_members_tmp = sorted(line.split(', '), key=str.lower)
      now_members = [x for x in now_members_tmp if x]
    res = {"now": now_size, "max": max_size, "players": now_members}
    f = open('/tmp/mine_users.json', 'w')
    f.write(json.dumps(res))
    f.close()
#    print(json.dumps(res))
#    int Ans = Num1 < Num2 ? Num1 : Num2;
