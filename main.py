import matplotlib.pyplot as plt
import networkx as nx
from urllib.request import urlopen
import json


file = urlopen("https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022")

flights = json.loads(file.read())
print(flights[0])

#G = nx.Graph()
G = nx.DiGraph()

#------------------------
# direct flights

for flight in flights:
    city1 = flight["city1"]
    city2 = flight["city2"]
    fare = float(flight["fare"])
    #print("Flight from " + city1 + " to " + city2)
    G.add_edge(city1, city2, weight=fare)

city1 = input("Enter first city: ")
city2 = input("Enter destination city: ")

cityFound = False

if G.has_edge(city1, city2):
  price = G[city1][city2]["weight"]
  print("Direct flight from " + city1 + " to " + city2 + " has a price of $" + price)
  G_path = nx.path_graph([city1, city2])
  position = nx.spring_layout(G_path)
  nx.draw(G_path, position, with_labels=True, font_weight='bold')
  nx.draw_networkx_edge_labels(G_path, position, edge_labels=nx.get_edge_attributes(G_path, "weight"))
  plt.show()
else:
  connections = []
  for connection in G.neighbors(city1):
    for destination in G.neighbors(connection):
      if G.has_edge(connection, destination) and G.has_edge(destination, city2):
        connections.append((connection, destination))

  if connections:
    min_fare = float("inf")
    for connection in connections:
      fare1 = G[city1][connection[0]]['weight']
      fare2 = G[connection[0]][connection[1]]['weight']
      fare3 = G[connection[1]][city2]['weight']
      total_fare = fare1 + fare2 + fare3
      if total_fare < min_fare:
        min_fare = total_fare
        best_connection = connection
    print("Connnecting flight found through " + best_connection[0] + " and " + best_connection[1] + ", fare: " + str(min_fare))
  else:
    print("No direct flight found between " + city1 + city2)


#------------------------------
#Non-direct flights


  






'''for x in y:
    if cityName in x["city1"]:
        cityFound = True
        city1 = x["city1"]
        city2 = x["city2"]
        print("Flight from " + city1 + " to " + city2 + fare)
        G.add_edge(city1, city2, weight=fare)

if not cityFound:
    print("City not found in the flights.")
'''

#G = nx.Graph()
#G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1,2),(1,3),(4,1),(2,4)])

pos_spaced = nx.fruchterman_reingold_layout(G, k=0.5, iterations=100)
plt.figure(figsize=(6,10)) # 6x10 inches
nx.draw(G, pos=pos_spaced, with_labels=True) 
nx.draw_networkx_edge_labels(G, pos_spaced,
              edge_labels = nx.get_edge_attributes(G,"weight"))
plt.show(block=False)





'''nx.draw(G, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(G,  nx.spring_layout(G), edge_labels = nx.get_edge_attributes(G, "weight"))


plt.show()'''