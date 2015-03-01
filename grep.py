import sys

def grep(pat, filename):
	lines = open(filename).readlines()
	list = []
	for i in lines:
		if pat in i:
			list.append(i)
	return "".join(list)

def main():
	pat = sys.argv[1]
	filename = sys.argv[2]
	print grep(pat,filename)

if __name__ == "__main__":
        main()
