import numpy as np
import matplotlib.pyplot as plt
from math import sqrt



idcounter = 1

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def createnode(layersize):
    """create a set of weights for a given node based on number of connections to the node"""
    node = np.array([])
    weights = np.array([])
    bias = 0
    for j in range(layersize):
        weights = np.append(weights, [np.random.uniform(0,1)])
    a = sqrt(6)/sqrt(layersize + layersize)
    bias = np.random.uniform(-a, a)
    node = np.append(node, [weights, bias])
    return node



class layer:
    """an object to store nodes as arrays"""
    def __init__(self, layersize, activationfunction, nextlayeri, prevlayeri):

        nodeweights = np.array([])
        nodebias = np.array([])

        for i in range(layersize):
            nodesample = createnode(layersize)
            nodeweights = np.append(nodeweights, nodesample[0])
            nodebias = np.append(nodebias, nodesample[1])
    

        #if layer does not have a node to connect to then it is output, if there is no node preceding it, it is input
        if prevlayeri == 0:
            self.prevlayer = 0 
        else:
            self.prevlayer = prevlayeri.idthing
        if nextlayeri == 0:
            self.nextlayer = 0
        else:
            self.nextlayer = nextlayeri.idthing

        #contains the list of weights of nodes and list of bias of nodes all in order
        self.weights = np.split(nodeweights, layersize)
        self.bias = nodebias
        global idcounter
        self.idthing = idcounter + 1
        idcounter += 1



#here numlayers is the number of TOTAL layers including input and output layers
def createnetwork(numlayers, layersize):


    #There are two arrays which collectively define a layer
    #first contains bias values for each node and the second contains an array of all the weights for the connections going ##OUT OF## each node
    #define the array that will hold the weight array and the bias array (both are in order)
    network = np.array([])

    #create the correct number of layers
    for k in range(numlayers):
        #if this is the first layer in the network (input layer), make a layer that is not connected on either end
        if network.size == 0:
            network = np.append(network, [layer(layersize, 'htan', 0, 0)])
        #if this is a hidden node, create a new templayer with the most recent layer in the network as its previous connection,
        #then add it to the network and connect the previous layer to this one
        elif network.size > 0 and network.size < numlayers:
            network = np.append(network, [layer(layersize, 'htan', 0, 0)])
            #connecting previous layer to this one
            network[-2].nextlayer = network[-1].idthing
            network[-1].prevlayer = network[-2].idthing
        else:
            network = np.append(network, layer(layersize, 'htan', 0, network[-1]))
    
    return network



network = createnetwork(100,10)
