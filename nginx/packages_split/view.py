#!/usr/bin/env python
from graphviz import Digraph
from glob import glob

class Node:
    name = None
    relationships = None
    _id = None

    def __init__(self, name, _id):
        self.name = name
        self._id = _id

def parse_node(filename):
    with open(filename) as fp:
        data = fp.read()

    ref = data[data.index("SPDXRef"):].split()[0]
    name = data[data.index("PackageName"):].split()[1]
    # walk through the relationships 
    chunks = data.split("Relationship:")[1:]

    relationships = []
    for chunk in chunks:
        new_ref, _type, otherref = chunk.strip().split(" ")
        if new_ref != ref:
            print(f'Extraneous relationship on {ref} with {new_ref} as source')
            continue
        relationships.append(otherref)

    # FIXME: should parse the name somewhere else
    node = Node(name, ref)
    node.relationships = relationships

    return node


graph = Digraph(comment='Dependency documentation')

for filename in glob("spdx_docs/*"):
    node = parse_node(filename)

    graph.node(node._id, node.name)
    for rel in node.relationships:
        graph.edge(node._id, rel)

graph.render('graph.png', view=True)
