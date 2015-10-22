"""module to run pagerank on a variety of datasets"""

from pagerank import PageRank

def returnSorted(d, limit = None):
   """Returns keys and values sorted by value by descending order"""
   
   result = sorted(d.items(), key=lambda x: x[1], reverse=True)
   if limit:
      return result
   return result[:limit]

def runStates():
   """run pagerank on stateborders.csv"""
   f = open('stateborders.csv')

   graph = PageRank()
   for line in f:
      column = line.split(',')
      left = column[0].strip('"')
      right = column[2].strip('"')
      graph.addEdge(left, right)

   graph.printGraph()
   iterations, ranks = graph.getPageRank()
   print "Number of iterations:", iterations
   print returnSorted(ranks)

if __name__ == '__main__':
   runStates()
