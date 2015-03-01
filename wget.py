import urllib
import sys

w = sys.argv[1]
def wget(w):
	return urllib.urlopen(w).read()

def getbase(w):
	return w.split("/")[-1]

def write(filename):
	f = open((filename),"w")
	f.write(wget(w))
	f.close()

def main():
	if w.endswith("/"):
		write("index.html")
		print "saving %s as index.html" % w
	else:
		write(getbase(w))
		print "saving %s as %s" % (w, getbase(w))

if __name__ == "__main__":
	main()
