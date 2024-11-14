
#def get_slice(str, a, b, c, d):
#    return(str[a:b+1], str[c:d+1])


#print(*get_slice("OHcJ5dWaCAMW7ilIAUmvcW622ik5rogudoz5tnHLplIdm33SGEnfR3skkiA2JqwjurdIovylKQ2CVjtHPhyllopneusteaiF6cVLn6BZQKPS3NKpLvg827oS8JBu9UxYojxBHwBvf2bTEJZsbEnngarmaniiEX5ZsP1ayINGb.",
#80, 92, 148, 154))



#def get_sum(a,b):
#    return sum([i for i in range(a, b+1) if (i % 2) != 0])

#print(get_sum(4418, 8974))

#lines = []

#with open("file.txt", "r") as file:
#    for i, line in enumerate(file):
#        if i % 2 != 0:
#            lines.append(line)
#print(*lines)

#with open("file2.txt", "w") as file:
#    for i in lines:
#        file.write(i)


Dict = {}

string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

for word in string.split(" "):
    if word not in Dict:
        Dict[word] = 1
    else:
        Dict[word] += 1

for key, value in Dict.items():
    print(key, value)
