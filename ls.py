import os
import sys

def listdir(dir):
	return os.listdir(dir)

def main():
	dir = sys.argv[1]
	print "\n".join(listdir(dir))

if __name__ == "__main__":
	main()
