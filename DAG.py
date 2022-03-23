
# not object oriented!!

class DAG:
    def __init__(self) -> None:
         nodes = []
         arcs = []

         nodes.append(Node(1))
         nodes.append(Node(2))         
         nodes.append(Node(3))

         arcs.append(nodes[0], nodes[1], 7)
         arcs.append(nodes[0], nodes[2], 10)
         arcs.append(nodes[1], nodes[2], 5)

class Node:
    def __init__(self, code: str) -> None:
        self.code = code
    

class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance




