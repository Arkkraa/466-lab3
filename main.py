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
      columns = line.split(',')
      left = columns[0].strip('"')
      right = columns[2].strip('"')
      graph.addEdge(left, right)

   graph.printGraph()
   iterations, ranks = graph.getPageRank()
   print "Number of iterations:", iterations
   print returnSorted(ranks)

def runFootball():
   """run pagerank on NCAA_football.csv"""

   f = open('NCAA_football.csv')
   graph = PageRank()

   for line in f:
      columns = line.split(',')
      team1 = columns[0].strip()
      value1 = int(columns[1])
      team2 = columns[2].strip()
      value2 = int(columns[3])

      if value1 > value2:
         graph.addEdge(team2, team1)

      elif value1 < value2:
         graph.addEdge(team1, team2)

      else:
         graph.addEdge(team2, team1)
         graph.addEdge(team1, team2)

   graph.printGraph()
   iterations, ranks = graph.getPageRank()
   print "Number of iterations:", iterations
   print returnSorted(ranks)


      
if __name__ == '__main__':
   #runStates()
   runFootball()
