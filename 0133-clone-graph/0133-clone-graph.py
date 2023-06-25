"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.nodeHashMap = {}
        return self.clone(node)
    
    def clone(self, node):
        if node == None:
            return None
        if node in self.nodeHashMap:
            return self.nodeHashMap[node]
        copy_node = Node(node.val)
        self.nodeHashMap[node] = copy_node

        listOfNodes = []
        if node.neighbors != None:
            for neighbor in node.neighbors:
                listOfNodes.append(self.clone(neighbor))
        # if len(listOfNodes) == 0:
        #     listOfNodes = None
        copy_node.neighbors = listOfNodes
        self.nodeHashMap[node].neighbors = listOfNodes
        return copy_node


            
        
        