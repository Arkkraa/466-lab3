# pagerank algorith
import math
import sys
import re
import string
import pprint

class PageRank:
   """A class that represents a graph used for pagerank"""
   
   def __init__(self):
      self.degree = {}
      self.destinations = {}
      self.rank = {}
      self.sources = {}

   def addNode(self, node):
      """Add a new source to the graph. Overwrites existing source with
      the same name"""
      if node not in self.degree:
         self.degree[node] = 0
         self.destinations[node] = []
         self.sources[node] = []

   def addDestination(self, source, target):
      """Add a new edge to the graph"""
      self.destinations[source].append(target)
      self.degree[source] = self.degree.get(source,0) + 1

      self.sources[target].append(source)

   def getDegree(self, node):
      """Return the degree of the given node"""
      return self.degree[node]

   def getDestinations(self, source):
      """Return a list of destinations for source"""
      return self.destinations[source]

   def printGraph(self):
      """Print out the graph"""

      for node in sorted(self.degree.keys()):
         print "%s\t%d\t%s" % (node, self.degree[node], self.destinations[node])

   def goodEnough(self, newPageRank, oldPageRank):
      """Check if pagerank has conveged"""
      epsilon = 0.00001
      sum = 0
      for node in newPageRank:
         sum += (newPageRank[node] - oldPageRank[node]) ** 2 
      
      return math.sqrt(sum) < epsilon

   def getPageRank(self):
      """Return the number of iterations it took to converge as well as the 
      pagerank of the graph"""

      numOfNodes = len(self.degree)
      for node in self.degree:
         self.rank[node] = 1.0 / numOfNodes 

      d = 0.8
      i = 1
      while True:
         newPageRank = {}
         for node in self.rank:
            sum = 0
            for source in self.sources[node]:
               sum += self.rank[source] / self.degree[source]

            newPageRank[node] = ((1 - d) / numOfNodes) + d * sum

         if (self.goodEnough(newPageRank, self.rank)):
            self.rank = newPageRank
            return i, self.rank

         self.rank = newPageRank
         i += 1

def getData(fp):
   """Create a PageRank graph from the file"""
   graph = PageRank()
   data = fp.read().splitlines()

   for line in data:
      nodes = re.split(r',', line)
      nodes = [col.strip(' ' + string.punctuation) for col in nodes]
      graph.addNode(nodes[0])
      graph.addNode(nodes[2])

      if int(nodes[1]) >= int(nodes[3]):
         graph.addDestination(nodes[2], nodes[0])
      else:
         graph.addDestination(nodes[0], nodes[2])

   return graph


if __name__ == '__main__':
   fname = sys.argv[1]
   fp = open(fname, 'r')

   graph = getData(fp)

   print 'pageRanks:'
   print graph.getPageRank()


   """
   graph.addNode('a')
   graph.addNode('b')
   graph.addNode('c')
   graph.addNode('d')

   graph.addDestination('a', 'b')
   graph.addDestination('a', 'd')
   graph.addDestination('a', 'c')

   graph.addDestination('b', 'a')
   graph.addDestination('b', 'd')

   graph.addDestination('c', 'c')

   graph.addDestination('d', 'b')
   graph.addDestination('d', 'c')
   graph.printGraph()
   
   print 'pageRanks:'
   print graph.getPageRank()
   """




         