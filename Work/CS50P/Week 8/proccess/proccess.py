import sys
import re

m_atches = []

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

elif len(sys.argv) == 2:
    with open(f"{sys.argv[1]}", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.lstrip()
            if matches := re.match(r"^#([0-9]+)", line):
                if (int(matches.group(1)), line) not in m_atches:
                    m_atches.append((int(matches.group(1)), line))
        m_atches.sort()
        for _, line in m_atches:
            print(line)
