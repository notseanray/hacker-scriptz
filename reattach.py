#!/usr/bin/python3
import os
import subprocess

def sessions():
    result = subprocess.Popen(["tmux", "ls"], stdout=subprocess.PIPE)
    sessions = []
    for line in result.stdout.read().splitlines():
        li = str(line).split(" ")
        try:
            sessions.append(int(li[0][2:-1]))
        except:
            pass
    return sessions
res = sessions()
if len(res) > 0:
    os.system("tmux a -t " + str(res[0]))
