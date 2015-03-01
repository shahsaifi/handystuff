import threading

def f(arg):
	name = threading.currentThread().getName()
	for i in range(10):
	    line = "%s %s %s" % (name, arg, i)
	    print line

def main():
	print "before thread creation"
	t1 = threading.Thread(target=f, args=("t1",))
	t2 = threading.Thread(target=f, args=("t2",))
	print "before start"
	t1.start()
	t2.start()
	print "after start"
	t1.join()
	t2.join()
	print "after join"

if __name__ == "__main__":
    main()
