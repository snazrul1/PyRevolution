__author__ = 'snazrul'

def getDoc(script)
	"""
	Extracts function description from Python script
	:param script [str] : path to script
	"""
	handle = open(script, 'r')
	doc = open(script+'_documentation.txt', 'a')

	write = False
	inFunc = False

	lines = handle.readlines()

	for line in lines:
	    if 'def' in line:
		doc.write(line[4::])
		inFunc = True

	    if '"""' in line:
		if (write == True) & (inFunc == True):
		    write = False
		    inFunc = False
		    doc.write('STATUS:\n\n\n')
		else:
		    write = True

	    if (write == True) & (inFunc == True) & ('"""' not in line):
		doc.write(line)

	handle.close()
	doc.close()

def main(args):
	for arg in args:
	getDoc(arg)

if __name__ == '__main__':
	main(sys.argv)
