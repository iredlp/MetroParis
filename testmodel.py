from model.fermata import Fermata
from model.model import Model

model = Model()
#model.buildGraph()

print("Numero nodi:",len(model.get_numnodi()))
model.buildGraph()
print("Numero archi:",len(model.get_numarchi()))

source=Fermata(2,"Abbesses", 2.33855, 48.8843) #paramentro importato a mano pdal DB per non dover fare altre query

nodiBFS=model.getBFSNodesFromEdges(source)
print(len(nodiBFS))
for i in range(0,10):
    print(nodiBFS[i])

nodiDFS=model.getDFSNodesFromEdges(source)
print(len(nodiDFS))
for i in range(0,10):
    print(nodiDFS[i])