import sys
import os
f = open("output.txt", "wt")
i = 0
while True:
    f.write("{}\n ".format(i))
    i+=1
    if i % 50 == 0:
        y = os.path.getsize('./output.txt')
        print("\rgenerated {} lines, size: ~{} mb".format(i, round(y/1000000)), end =' ')
        sys.stdout.flush()
