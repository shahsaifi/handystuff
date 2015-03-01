import sys

def linecount(filename):
	return len(open(filename).readlines())

def wordcount(filename):
        return len(open(filename).read().split())

def charcount(filename):
        return len(open(filename).read())

def main():
      filename = sys.argv[1]
      print linecount(filename), wordcount(filename), charcount(filename), filename

if __name__ == "__main__":
      main()
