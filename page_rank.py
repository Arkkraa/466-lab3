import re
import pprint
import string
import sys

def get_data(fp):

	data = fp.read().splitlines()

	graph = {}

	for line in data:
		nodes = re.split(r',', line)
		nodes = [col.strip(' ' + string.punctuation) for col in nodes]
		
		if nodes[1] >= nodes[3]:
			adj = graph.get(nodes[0], [])
			adj.append(nodes[2])
			graph[nodes[0]] = adj
	pprint.pprint(graph)

if __name__ == '__main__':
	try: 
		fname = sys.argv[1]
		fp = open(fname, 'r')
		get_data(fp)
	except Exception:
		print "usage: page_rank.py <file>"


