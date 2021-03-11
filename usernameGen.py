import rstr, sys, time

startTime = time.time()

names = [] # Do not touch

MAX = sys.argv[1] # Amount of Usernames
LEN = sys.argv[2] # Username Length

def genString(length):
	name = rstr.xeger("^[a-zA-Z0-9][\w]{"+str(int(int(length)-1))+"}$")
	if name.lower() in names:
		return str(name + " - DUPLICATE")
	else:
		names.append(name.lower())
		return name

for x in range(int(MAX)):
	print(genString(LEN), x)

print("Generated "+str(len(names))+" names. - Took "+str(round(time.time() - startTime, 2))+" seconds.")
f = open("names.txt", "w")
f.write("\n".join(names))
f.close()