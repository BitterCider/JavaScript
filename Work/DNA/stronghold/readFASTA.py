#Call functions and print result

def main():
    content = FASTAhandle("FASTA1.txt")
    result = GC_count(content)
    print(f"\n{max(result, key=result.get)} <<<")
    for key, value in result.items():
        print(f"\n{key}\n{round(value, 6)}%")


# Handle FASTA format

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

#Count GC Content in sequences

def GC_count(dict):
    gc_content = {}
    for key, seq in dict.items():
        G_content = seq.count("G")
        C_content = seq.count("C")
        gc_content[key] = (G_content + C_content)/len(seq)*100
    return gc_content


if __name__ == "__main__":
    main()
