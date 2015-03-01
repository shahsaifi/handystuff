import sys

def headline(filename):
	return "".join(open(filename).readlines()[0:10])

def tailline(filename):
	return "".join(open(filename).readlines()[-10:])

def main():
	filename = sys.argv[1]
	print "Heading ..."
	print headline(filename)
	print "Tailing ..."
	print tailline(filename)

if __name__ == "__main__":
        main()
