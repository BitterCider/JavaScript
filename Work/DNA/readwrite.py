
def readfile(filepath):
    with open(filepath, "r") as file:
        lines = [l.strip() for l in file]
    return lines

def writefile(filename, seq, mode="w"):
    with open(filename, mode) as file:
        file.write(seq + "\n")

# handle FASTA format, returns dictionary 

def FASTAhandle(file):
    with open(file, 'r') as file:
        FASTAlist = [line.strip() for line in file]
    # create empty dict to store lable and sequence
    FASTAdict = {}
    for line in FASTAlist:
        if ">" in line:
            FASTAlable = line.replace(">", "")
            FASTAdict[FASTAlable] = ""
        else:
            FASTAdict[FASTAlable] += line
    return FASTAdict
