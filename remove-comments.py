import sys

args = sys.argv
if len(args) < 2:
    print("please specify file(s) to run on")

args.pop(0)
save = False

if "--save" in args:
    save = True
    args.remove("--save")

for file in args:
    contents = ""
    f = open(file)
    for line in f.readlines():
        pos = line.find("#")
        if pos >= 0:
            in_quote = line.find('"')
            if in_quote >= 0:
                if len(line) < in_quote:
                    continue
                end_quote = line[in_quote + 1:].find('"')
                if pos > in_quote and pos <= in_quote + end_quote + 1:
                    contents += line
                    continue
            in_quote = line.find("'")
            if in_quote >= 0:
                if len(line) < in_quote:
                    continue
                end_quote = line[in_quote + 1:].find("'")
                if pos > in_quote and pos <= in_quote + end_quote + 1:
                    contents += line
                    continue
            new_line = line[0:pos].rstrip()
            if len(new_line) <= 0 or len(new_line.strip()) == 0:
                continue
            contents += line[0:pos] + "\n"
        else:
            contents += line
    print(contents) 
    if save:
        f = open(file + "decommented", "w")
        f.write(contents)
        f.close()
