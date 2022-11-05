#!/bin/python3
import os
import sys

mksh_shebang = "#!" + os.popen("whereis zsh").readline().split(" ")[1] + "\n"

print("found mksh at: " + mksh_shebang)

def replace_bash(file):
    flag = True
    file_open = open(file, "r")
    file_contents = file_open.readlines()
    if len(file_contents) < 1:
        return
    if file_contents[0] == "#!/bin/bash\n" or file_contents[0] == "#!/bin/mksh":
        file_contents[0] = mksh_shebang
        flag = False
    if flag:
        return
    print("replacing shebang for file: " + file)
    file_open.close()
    write = open(file, "w")
    write.writelines(file_contents)

arg = sys.argv[2:]

if len(arg) == 0 or arg.__contains__("."):
    for file in os.listdir("."):
        print(file)
        replace_bash(file)
else:
    for argument in arg:
        print(argument)
        replace_bash(argument)
