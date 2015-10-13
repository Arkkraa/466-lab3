import re
import pprint
import string
import sys

def get_data(fp):
	nodes = {}

	data = fp.read().splitlines()
	for line in data:
		line = re.split(r',', line)
		line = [col.strip(string.punctuation) for col in line]
		nodes[line[0]] = (line[1], line[2])

	#pprint.pprint(nodes)


if __name__ == '__main__':
	try: 
		fname = sys.argv[1]
	except Exception:
		print "usage: page_rank.py <file>"

	#fp = open('NCAA_football.csv', 'r')
	#data_ncaa = get_data(fp)
	#fp.close()



	"""fp = open('stateborders.csv', 'r')
	data_borders = get_data(fp)
	fp.close()
	fp = open('karate.csv', 'r')
	data_karate = get_data(fp)"""

